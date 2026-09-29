#!/usr/bin/env python3
"""Stage the reviewed communication collection for GitHub and download."""
import hashlib
import json
import shutil
import zipfile
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'publish' / 'materials'
ORDER = ['iclr2027', 'aistats2027', 'uai2026', 'kg-uncertainty', 'factor-regime', 'regime-predictability', 'icaif2026']
KINDS = ['slides_en.pptx', 'slides_en.pdf', 'poster_en.pdf', 'introduction_en.pdf', 'introduction_ko.pdf']

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    entries = []
    assets = set()
    for ident in ORDER:
        data = json.loads((ROOT/'content'/f'{ident}.json').read_text())
        assert len(data['slides']) == 10, ident
        out = DEST/ident
        out.mkdir(exist_ok=True)
        artifacts = []
        for kind in KINDS:
            src = ROOT/'output'/ident/kind
            target = out/f'{ident}_{kind}'
            shutil.copyfile(src, target)
            item = {'kind': kind, 'path': str(target.relative_to(DEST)), 'sha256': digest(target), 'bytes': target.stat().st_size}
            if target.suffix == '.pdf':
                doc = fitz.open(target)
                expected = 10 if kind.startswith('slides') else 1
                assert len(doc) == expected, (ident, kind, len(doc))
                item['pages'] = len(doc)
                item['page_size_pt'] = [round(doc[0].rect.width, 2), round(doc[0].rect.height, 2)]
                doc.close()
            artifacts.append(item)
        for lang in ['en','ko']:
            src = ROOT/'output'/ident/f'introduction_{lang}.md'
            shutil.copyfile(src, out/f'{ident}_introduction_{lang}.md')
        for obj in data['slides']+[data['poster']]:
            if obj.get('figure', {}).get('path'):
                path = Path(obj['figure']['path'])
                path = path.relative_to(ROOT) if path.is_absolute() else path
                obj['figure']['path'] = str(path)
                assets.add(path)
                if (ROOT/path.with_suffix('.pdf')).exists():
                    assets.add(path.with_suffix('.pdf'))
        (DEST/'content').mkdir(exist_ok=True)
        (DEST/'content'/f'{ident}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
        entries.append({'id':ident,'title':data['title'],'short_title':data['short_title'],'source':data['source'],'artifacts':artifacts})
    for asset in assets:
        (DEST/asset).parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/asset,DEST/asset)
    for name in ['concentration_evidence.svg','replot.py','concentration_evidence_data.json','source_generate_n16_figure.py']:
        asset=Path('assets/uai2026')/name
        (DEST/asset).parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/asset,DEST/asset)
    shutil.copytree(ROOT/'assets/fonts', DEST/'assets/fonts', dirs_exist_ok=True)
    (DEST/'tools').mkdir(exist_ok=True)
    for name in ['build_decks.mjs','build_print.py','package_collection.py','check_deck_pdfs.py']:
        shutil.copyfile(ROOT/'tools'/name,DEST/'tools'/name)
    shutil.copytree(ROOT/'reviews',DEST/'reviews',dirs_exist_ok=True)
    manifest={'prepared':'2026-09-29','author':'Chorok Lee','deliverables':35,'slide_count_per_deck':10,'poster_format':'A0 portrait, English','introduction_format':'A4, one page per language','papers':entries}
    (DEST/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    archive=DEST/'research_materials_2026-09-29.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for entry in entries:
            for artifact in entry['artifacts']:
                z.write(DEST/artifact['path'],artifact['path'])
        z.writestr('SOURCE_VERSIONS.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        for path in sorted((DEST/'assets/fonts').glob('*')):
            if path.is_file():
                z.write(path,str(path.relative_to(DEST)))
    lines=['# Research communication materials','','Chorok Lee, KAIST. Prepared 29 September 2026.','',
           'Seven source-grounded presentation sets: each includes an English 10-slide deck, an English A0 poster, and separate English and Korean A4 introductions. Each introduction is exactly one page.','',
           '[Download all 35 presentation files](research_materials_2026-09-29.zip)','',
           '| Paper | Slides (English, 10 pages) | Poster (English, A0) | Introduction (1 page each) |','| --- | --- | --- | --- |']
    for e in entries:
        i=e['id'];base=f'{i}/{i}_'
        lines.append(f"| **{e['short_title']}** | [PPTX]({base}slides_en.pptx) · [PDF]({base}slides_en.pdf) | [PDF]({base}poster_en.pdf) | [English]({base}introduction_en.pdf) · [한국어]({base}introduction_ko.pdf) |")
    lines += ['', '## Source versions', '',
              'The materials follow the exact manuscript revisions below. They may be newer than the catalogue’s older one-minute speeches and one-pagers. The Factor Decay set follows the original ten-page TeX preprint, separately from the five-page submission record.', '',
              '| Paper | Source revision |', '| --- | --- |']
    for e in entries:
        s=e['source'];lines.append(f"| {e['short_title']} | [{s['commit'][:12]}]({s['url']}) |")
    lines += ['', '## Review and revision', '',
              'Content authors and an independent reviewer exchanged source-located critiques before the final build. Review covered numerical denominators, timing assumptions, theoretical scope, interpretation of null results, and Korean wording. The design review inspected rendered slides, posters and introductions, then corrected spacing, missing mathematical glyphs and source-version labels.', '',
              'The [review records](reviews/) document the discussions and resulting changes. This was an agent review of communication materials. It does not replace scientific peer review or a rerun of the underlying experiments.', '',
              '## Editable sources and rebuilding', '',
              '- PPTX text and tables are editable. Speaker notes include explanations and source references.',
              '- The slide design uses Noto Sans. Install the bundled fonts for matching PowerPoint line wraps; the PDFs embed fonts and preserve the reviewed layout.',
              '- English and Korean introduction Markdown files sit beside the PDFs. Shared content is in [content/](content/).',
              '- Print PDFs use `python tools/build_print.py` with ReportLab, PyMuPDF and Pillow. Font files and their licenses are in `assets/fonts/`.',
              '- Slides use `tools/build_decks.mjs` with the OpenAI artifact-tool runtime and LibreOffice. This builder requires that runtime and its presentation validation helpers; the editable PPTX files do not.',
              '- Builders write into `output/`; `python tools/package_collection.py` stages prefixed final filenames and the ZIP under `publish/materials/`.',
              '- [manifest.json](manifest.json) records source identities, page counts, file sizes and SHA-256 hashes.', '',
              'The posters are A0 portrait (841 × 1189 mm). Print at actual size. Slides are 16:9. No conference acceptance or arXiv publication status is inferred from preparation of these materials.', '']
    (DEST/'README.md').write_text('\n'.join(lines))
    (DEST/'.gitignore').write_text('output/\npublish/\nqa/\n.deck-build/\n__pycache__/\n')
    print(json.dumps({'destination':str(DEST),'deliverables':35,'archive':str(archive),'bytes':archive.stat().st_size},indent=2))

if __name__ == '__main__':
    main()
