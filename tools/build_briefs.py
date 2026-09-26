#!/usr/bin/env python3
"""Build README and seven bilingual PDF briefs from reviewed local metadata.

Install reportlab, then set BRIEF_FONT_DIR to a directory containing
NanumGothic-Regular.ttf and NanumGothic-Bold.ttf (Google Fonts, OFL).
PDF creation is deterministic; it performs no network requests.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_KO = {
    'Reliable prediction and statistical evaluation': '예측 신뢰성과 통계적 평가',
    'Knowledge graphs and error diagnosis': '지식 그래프와 오류 진단',
    'Financial forecasting and model evaluation': '금융 예측과 모델 평가',
}


def url(p, key):
    path = p.get(key)
    return f"{p['repository_url']}/blob/{p['branch']}/{path}" if path else None


def readme(papers, briefs):
    lines = [
        '# Research Papers', '',
        'Chorok Lee · Private research catalogue · Updated 27 September 2026', '',
        '논문별 저장소, 기준 원고, 한 페이지 소개와 한·영 1분 스피치를 모았습니다. '
        '범위는 지정한 여섯 저장소와 추가 요청한 ICAIF 제출본입니다. '
        '아래 7개 항목은 프로젝트/버전 목록이며 독립적인 출판 논문 수를 뜻하지 않습니다.', '',
        '## Papers', '',
    ]
    for category, ko in CATEGORY_KO.items():
        lines += [f'### {category}', '', f'*{ko}*', '',
                  '| Paper / version | Manuscript | arXiv source | One-pager |',
                  '| --- | --- | --- | --- |']
        for p in papers:
            if p['category'] != category:
                continue
            arxiv = f"[ZIP]({url(p, 'arxiv_source')})" if p.get('arxiv_source') else '—'
            lines += [f"| **{p['label']}** · [{p['title']}]({p['working_branch_url']})<br>{p['status']} | [PDF]({url(p, 'manuscript')}) | {arxiv} | [EN / KO PDF]({p['one_pager']}) |"]
        lines.append('')
    lines += [
        '### Version notes', '',
        '- **ICLR:** the current repository is `selective-labels-minimax-iclr2027`; manuscript and source links use its cleaned `artifacts/` and `paper/` layout.',
        '- **ICAIF:** submission **239**, **decision pending**. The author-supplied five-page PDF is authoritative. The related ten-page manuscript and code are an earlier provenance snapshot; the exact submitted LaTeX source was not located. The arXiv ZIP is a documented reconstruction with author identification and small consistency corrections. [arXiv PDF](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv.pdf) · [Title / abstract](https://github.com/ChorokLeeDev/factor-decay-icaif2026/tree/main/arxiv) · [Provenance](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/PROVENANCE.md) · [Version comparison](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/docs/VERSION_COMPARISON.md).',
        '- **Research lineage:** ICAIF and the regime-predictability revision share earlier research history. Their current claims and versions are tracked separately; later revision findings are not retroactively attributed to the ICAIF submission.',
        '- **Revision branches:** the three revision projects link to their active branches rather than possibly older default-branch manuscripts. Summaries record the exact source commits in [papers.json](papers.json). Live branch links may advance after the summary date.',
        '- **Status:** venue labels identify the tracked version. Only explicitly stated decisions should be read as conference outcomes. Repository preparation does not upload or alter a conference submission.', '',
        '## One-minute research introductions', '',
        'English scripts contain approximately 130 words each. English and Korean versions are intended as natural spoken introductions; timing varies with speaking pace. The linked one-pagers give the question, method, findings, limits and source version.', '',
    ]
    for p in papers:
        b = briefs[p['id']]
        lines += [f"### {p['label']}: {p['title']}", '',
                  f"[Repository]({p['working_branch_url']}) · [Paper PDF]({url(p, 'manuscript')}) · [One-pager]({p['one_pager']})", '',
                  '**English · about one minute**', '', b['speech_en'], '',
                  '**한국어 · 약 1분**', '', b['speech_ko'], '']
    lines += ['## Maintenance', '',
              '- Edit `papers.json` for links, statuses and source identities; edit `briefs.json` for the reviewed summaries and speeches.',
              '- Rebuild with `python tools/build_briefs.py`. See [one-pager build notes](one-pagers/README.md) for fonts and dependencies.',
              '- Update the source commit and review the scientific claims whenever a summary changes. Preserve submitted artifacts and distinguish reported results from newly reproduced evidence.', '']
    (ROOT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')


def pdf_briefs(papers, briefs, font_dir):
    for name, filename in [('Nanum', 'NanumGothic-Regular.ttf'), ('NanumBold', 'NanumGothic-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily('Nanum', normal='Nanum', bold='NanumBold')
    navy = colors.HexColor('#142D46')
    teal = colors.HexColor('#007F83')
    body = ParagraphStyle('Body', fontName='Nanum', fontSize=9.3, leading=13.2,
                          textColor=navy, spaceAfter=8, wordWrap='CJK')
    heading = ParagraphStyle('Heading', parent=body, fontName='NanumBold', fontSize=9.3,
                             leading=12, textColor=teal, spaceBefore=5, spaceAfter=3)
    title = ParagraphStyle('Title', parent=body, fontName='NanumBold', fontSize=17,
                           leading=21, spaceAfter=10)
    small = ParagraphStyle('Small', parent=body, fontSize=7.4, leading=10, spaceAfter=4)
    question = ParagraphStyle('Question', parent=body, fontName='NanumBold', fontSize=11,
                              leading=15, spaceAfter=10)
    out = ROOT / 'one-pagers'
    out.mkdir(exist_ok=True)
    manifest = []
    for index, p in enumerate(papers, 1):
        b = briefs[p['id']]
        target = out / (p['id'] + '.pdf')
        doc = SimpleDocTemplate(str(target), pagesize=A4, rightMargin=43, leftMargin=43,
                                topMargin=42, bottomMargin=39, title=p['title'],
                                author='Chorok Lee', subject='Research one-pager; source-grounded EN/KO summary',
                                invariant=1)
        story = [Paragraph(escape(p['category'].upper()), small),
                 Paragraph(escape(p['title']), title),
                 Paragraph(escape(b['status'] + ' | Summary: 27 September 2026'), small),
                 Spacer(1, 8), Paragraph(escape(b['question']), question)]
        for label, key in [('CENTRAL IDEA', 'idea'), ('MAIN FINDING', 'result'),
                           ('EVIDENCE AND SCOPE', 'evidence'), ('LIMITS', 'limitation'),
                           ('TAKEAWAY', 'takeaway'), ('한국어 핵심 요약', 'ko_summary')]:
            story.append(KeepTogether([Paragraph(escape(label), heading), Paragraph(escape(b[key]), body)]))
        source_id = p.get('summary_source_commit')
        source_text = ('Source commit: ' + source_id[:12]) if source_id else 'Source: actual five-page submission; SHA-256 ' + p['summary_source_sha256'][:16] + '...'
        story += [Spacer(1, 5), Paragraph(escape(source_text), small),
                  Paragraph(f'<link href="{escape(url(p, "manuscript"))}" color="#007F83">Read manuscript</link>  |  '
                            f'<link href="{escape(p["working_branch_url"])}" color="#007F83">Open repository</link>  |  '
                            '<link href="https://github.com/ChorokLeeDev/research-papers" color="#007F83">EN / KO one-minute speech</link>', small)]
        def page(canvas, document, number=index):
            canvas.setFillColor(teal)
            canvas.rect(0, A4[1]-8, A4[0], 8, fill=1, stroke=0)
            canvas.setFont('Nanum', 7)
            canvas.setFillColor(navy)
            canvas.drawString(43, 22, 'CHOROK LEE / RESEARCH BRIEFS')
            canvas.drawRightString(A4[0]-43, 22, f'{number:02d} / 07')
        doc.build(story, onFirstPage=page, onLaterPages=page)
        manifest.append({'id':p['id'], 'file':p['one_pager'], 'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--readme-only', action='store_true')
    args = parser.parse_args()
    papers = json.loads((ROOT/'papers.json').read_text())['papers']
    briefs = json.loads((ROOT/'briefs.json').read_text())
    assert len(papers) == 7 and {p['id'] for p in papers} == set(briefs)
    readme(papers, briefs)
    if not args.readme_only:
        font_dir = Path(os.environ.get('BRIEF_FONT_DIR', ROOT/'assets/fonts'))
        pdf_briefs(papers, briefs, font_dir)


if __name__ == '__main__':
    main()
