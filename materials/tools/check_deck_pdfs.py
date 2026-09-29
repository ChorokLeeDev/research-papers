#!/usr/bin/env python3
"""Inspect final PDF exports and render representative slides for visual QA."""
from pathlib import Path
import json, re, sys
import fitz
ROOT=Path(__file__).resolve().parent.parent
FALLBACK_SYMBOLS='→√≤≥≈'

def norm(s):
    return re.sub(r'\s+', '', str(s)).replace('\u2011','-')

def prose_norm(s):
    # LibreOffice writes fallback-font glyphs in later PDF content spans.
    # Verify surrounding text separately, and explicitly count those glyphs.
    return norm(s).translate(str.maketrans('', '', FALLBACK_SYMBOLS))

out=[]
for f in sorted((ROOT/'content').glob('*.json')):
    doc=json.loads(f.read_text());id=doc['id'];pdf=fitz.open(ROOT/'output'/id/'slides_en.pdf')
    assert len(pdf)==10,(id,len(pdf))
    checks=[]
    for i,(page,slide) in enumerate(zip(pdf,doc['slides'])):
        assert abs(page.rect.width/page.rect.height-16/9)<.005
        text=page.get_text();expected=[]
        if i==0: expected=[doc['title'],'Chorok Lee','KAIST']
        else:
            expected+=[slide['title']]
            if slide.get('lead'):expected.append(slide['lead'])
            expected+=slide.get('bullets',[])
            for c in slide.get('columns',[]):expected +=[c['heading'],c['body']]
            if slide.get('equation'):expected +=[slide.get('equation_plain',slide['equation'])]
            if slide.get('table'):
                expected+=slide['table']['headers']
                for r in slide['table']['rows']:expected+=r
            if slide.get('figure'):expected += [slide['figure']['caption']]
        raw_missing=[x for x in expected if norm(x) not in norm(text)]
        reordered=[x for x in raw_missing if prose_norm(x) in prose_norm(text)]
        missing=[x for x in raw_missing if prose_norm(x) not in prose_norm(text)]
        expected_join=''.join(str(x) for x in expected)
        symbol_shortfalls={c:{'expected':expected_join.count(c),'extracted':text.count(c)} for c in FALLBACK_SYMBOLS if expected_join.count(c)>text.count(c)}
        clipped=[]
        for b in page.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                for sp in l['spans']:
                    x0,y0,x1,y1=sp['bbox']
                    if x0<-.5 or y0<-.5 or x1>page.rect.width+.5 or y1>page.rect.height+.5:clipped.append(sp['text'])
        checks.append({'slide':i+1,'expected_items':len(expected),'missing_extracted_text':missing,'fallback_symbols_reordered_in_extraction':reordered,'fallback_symbol_shortfalls':symbol_shortfalls,'out_of_page_spans':clipped,'replacement_characters':text.count('\ufffd')})
    qa=ROOT/'qa'/id/'slides_pdf';qa.mkdir(exist_ok=True,parents=True)
    selected={0}
    eq=next((i for i,s in enumerate(doc['slides']) if s['layout']=='equation'),None)
    if eq is not None:selected.add(eq)
    tab=next((i for i,s in enumerate(doc['slides']) if s['layout']=='table'),None)
    if tab is not None:selected.add(tab)
    dense=max(range(1,10),key=lambda i:len(json.dumps(doc['slides'][i].get('table',{})))) if any(s.get('table') for s in doc['slides']) else 8
    selected.add(dense)
    if id=='uai2026':selected.add(4)
    if id=='icaif2026':selected.add(4)
    if id=='aistats2027':selected.update({5,7})
    if id=='regime-predictability':selected.update({5,6})
    for i in sorted(selected): pdf[i].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False).save(qa/f'slide-{i+1}.png')
    out.append({'id':id,'page_count':len(pdf),'checks':checks,'rendered_pages':[i+1 for i in sorted(selected)]})
(ROOT/'qa'/'deck_pdf_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
for item in out:
 print(item['id'], 'pages=',item['page_count'],'rendered=',item['rendered_pages'],'missing_items=',sum(len(c['missing_extracted_text']) for c in item['checks']),'offpage=',sum(len(c['out_of_page_spans']) for c in item['checks']))
