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
        'Chorok Lee · Research catalogue · Updated 29 September 2026', '',
        '논문별 저장소, 기준 원고, 한 페이지 소개와 한·영 1분 스피치를 모았습니다. '
        '금융 논문 세 편의 차이는 아래 비교표에서 확인할 수 있습니다. '
        '아래 7개 항목은 프로젝트/버전 목록이며 독립적인 출판 논문 수를 뜻하지 않습니다.', '',
        "## Research communication materials",
        "",
        "[**Open the full collection**](materials/README.md) · [Download all files](materials/research_materials_2026-09-29.zip)",
        "",
        "각 논문별 **영어 10장 발표 슬라이드(PPTX·PDF), 영어 A0 포스터, 영어·한국어 각각 1쪽 소개서**를 제공합니다. 총 7세트이며, 아래의 기존 1분 스피치·소개서와 별도로 제작했습니다. 원고 기반 내용 검토와 에이전트 간 교차 피드백을 반영한 자료입니다.",
        "",
        "The collection records exact manuscript revisions and review changes. Factor Decay follows the original ten-page TeX preprint. [Source versions and review records](materials/README.md#source-versions).",
        '', '## Papers', '',
    ]
    for category, ko in CATEGORY_KO.items():
        lines += [f'### {category}', '', f'*{ko}*', '',
                  '| Paper / version | Manuscript | arXiv source | One-pager |',
                  '| --- | --- | --- | --- |']
        for p in papers:
            if p['category'] != category:
                continue
            arxiv = f"[ZIP]({url(p, 'arxiv_source')})" if p.get('arxiv_source') else '—'
            manuscript = f"[PDF]({url(p, 'manuscript')})"
            if p.get('arxiv_url'):
                manuscript += f" · [arXiv]({p['arxiv_url']})"
            if p['id'] == 'icaif2026':
                manuscript = (f"[Preprint · 10 pages]({url(p, 'arxiv_pdf')})<br>"
                              f"[Submission · 5 pages]({url(p, 'manuscript')})")
            lines += [f"| **{p['label']}** · [{p['title']}]({p['working_branch_url']})<br>{p['status']} | {manuscript} | {arxiv} | [EN / KO PDF]({p['one_pager']}) |"]
        lines.append('')
    lines += [
        '### How the three finance papers differ', '',
        '**세 논문의 질문은 각각 “큰 손실의 전조인가?”, “예측에 도움이 되는 정보인가?”, “그 예측관계가 언제 약해지는가?”입니다.**', '',
        '| Paper | 쉬운 질문과 예시 | Main focus / 핵심 초점 |',
        '| --- | --- | --- |',
        '| **[Return-Decay Residuals](https://arxiv.org/abs/2512.11913)** | 투자전략의 성적 악화가 다음 달 큰 손실의 전조일까?<br>예: 모멘텀 전략의 성적이 예상보다 나빠졌을 때 이후 손실 위험도 커지는가? | **Tail-risk warnings · 손실 위험**<br>전략 자체의 성적에서 만든 지표가 미래 위험을 예측하는지, 같은 시점의 정보가 겹쳐 생긴 연관성인지 점검합니다. |',
        '| **[Source Exclusion](https://arxiv.org/abs/2601.10732)** | A의 정보를 알면 B를 더 잘 예측할 수 있을까?<br>예: 가치주 움직임을 알면 소형주 수익률 예측이 나아지는가? | **Value of source information · 정보의 예측 기여**<br>A를 예측식뿐 아니라 시장 국면 추정과 학습 과정에서도 완전히 빼고 비교하는 방법을 연구합니다. |',
        '| **[Predicting Factor Decay](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv.pdf)** | 관측된 A→B 예측관계는 얼마나 오래 유지될까?<br>예: 과거에 유용했던 가치주→소형주 관계가 언제 약해지는가? | **Durability of predictive relationships · 예측관계의 지속기간**<br>관계가 약해지는 시점과 위험을 생존 분석·머신러닝으로 예측할 수 있는지 탐색합니다. |', '',
        'The distinction is **future loss risk**, **the predictive contribution of a source**, and **the durability of a predictive relationship**. The last two papers share research history but ask different questions.', '',
        '여기서 팩터는 가치주·소형주·모멘텀처럼 공통된 투자 특성을 묶은 수익률을 뜻합니다. 첫 논문은 개별 전략의 성적과 손실 위험을, 나머지 두 논문은 팩터 사이의 예측관계를 다룹니다. 관계의 지속기간을 해석하려면 정보의 기여부터 제대로 측정해야 하므로 Source Exclusion의 검증 문제는 Factor Decay에도 중요합니다. 다만 특정 모델의 표본 외 실패만으로 실제 예측정보가 사라졌다고 단정할 수는 없습니다.', '',
        '**Evidence limits:** the two audit papers do not establish a robust general forecasting advantage. Factor Decay reports exploratory results based on only seven decay events; the comparison above describes research questions, not proven trading benefits.', '',
        '### Version notes', '',
        '- **ICLR:** the current repository is `selective-labels-minimax-iclr2027`; manuscript and source links use its cleaned `artifacts/` and `paper/` layout.',
        '- **Factor Decay preprint:** the current [PDF](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv.pdf) and [arXiv source ZIP](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/factor_decay_arxiv_source.zip), prepared on 29 September 2026, use the **ten-page original TeX edition**, with six figures and 21 references. This replaces the earlier reconstructed upload package. The abstract and research text are preserved from the original TeX; author details and the publication wrapper were updated, and the missing figure was recovered from the original reference PDF. [Editable source](https://github.com/ChorokLeeDev/factor-decay-icaif2026/tree/main/arxiv/original-source-20260929) · [Provenance](https://github.com/ChorokLeeDev/factor-decay-icaif2026/blob/main/arxiv/PROVENANCE.md). Package preparation does not establish arXiv publication or newly validate the experiments.',
        '- **ICAIF submission record:** the separate five-page submitted PDF remains authoritative for that submission. The existing ICAIF one-pager and one-minute introduction below describe that five-page version; they are not new summaries of the ten-page preprint. The exact submitted LaTeX source was not located.',
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
              '- Rebuild only this README with `python tools/build_briefs.py --readme-only`, or include the PDFs with `python tools/build_briefs.py`. The finance comparison and version notes are maintained in the README builder. See [one-pager build notes](one-pagers/README.md) for fonts and dependencies.',
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
