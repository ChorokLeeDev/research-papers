#!/usr/bin/env python3
"""Generate A0 English posters and A4 bilingual one-page introductions.
Usage: python tools/build_print.py [paper-id ...]
"""
from pathlib import Path
import argparse, json, re, math, html, shutil, subprocess
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A0
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import fitz

ROOT=Path(__file__).resolve().parents[1]
FONTROOT=ROOT/'assets/fonts'
NAVY='#102A43'; SLATE='#354F62'; MUTED='#607585'; LIGHT='#F1F6F7'; RULE='#D8E2E7'
for name,path in [('Sans',FONTROOT/'NotoSans-Regular.ttf'),('SansBold',FONTROOT/'NotoSans-Bold.ttf'),('Symbols',FONTROOT/'DejaVuSans.ttf'),('Korean',ROOT/'assets/fonts/NanumGothic-Regular.ttf'),('KoreanBold',ROOT/'assets/fonts/NanumGothic-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(path)))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold',italic='Sans',boldItalic='SansBold')
pdfmetrics.registerFontFamily('Korean',normal='Korean',bold='KoreanBold',italic='Korean',boldItalic='KoreanBold')

def clean(s):
    s=str(s or '').replace('\u2011','-').replace('\u2013','-').replace('\u2014',' - ').replace('−','-')
    return s

def para(text,size=11,font='Sans',color=SLATE,leading=None,align=0):
    raw=clean(text)
    cmap=pdfmetrics.getFont(font).face.charWidths
    text=''.join(html.escape(ch) if ord(ch) in cmap or ord(ch)<32 else '<font name="Symbols">'+html.escape(ch)+'</font>' for ch in raw).replace('\n','<br/>')
    # Only conservative inline emphasis markup supported in authored content.
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    return Paragraph(text,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.4,textColor=colors.HexColor(color),alignment=align,spaceAfter=0,allowWidows=0,allowOrphans=0,wordWrap=None))

def ph(p,w): return p.wrap(w,100000)[1]
def put(c,p,x,y,w):
    h=ph(p,w); p.drawOn(c,x,y-h); return y-h

def line(c,x,y,w,color=RULE,width=1):
    c.setStrokeColor(colors.HexColor(color));c.setLineWidth(width);c.line(x,y,x+w,y)

def image_fit(c,path,x,y,w,h,raster_only=False):
    path=Path(path)
    if not path.is_absolute(): path=ROOT/path
    if not path.exists() and '/assets/' in str(path): path=ROOT/'assets'/str(path).split('/assets/',1)[1]
    # Preserve original vector evidence whenever the source PDF accompanies a PNG.
    vector=path if path.suffix.lower()=='.pdf' else path.with_suffix('.pdf')
    if vector.exists() and raster_only:
        # Original figure uses transparency that differs across PDF compositors.
        # Composite its unchanged drawing onto white at 432 dpi for stable print colors.
        src=fitz.open(vector);pix=src[0].get_pixmap(matrix=fitz.Matrix(6,6),alpha=False);src.close()
        cached=ROOT/'tmp'/(vector.parent.name+'_'+vector.stem+'_print.png');cached.parent.mkdir(exist_ok=True);pix.save(cached)
        iw,ih=Image.open(cached).size;f=min(w/iw,h/ih);dw=iw*f;dh=ih*f
        c.drawImage(str(cached),x+(w-dw)/2,y-h+(h-dh)/2,width=dw,height=dh,mask='auto')
    elif vector.exists():
        src=fitz.open(vector);iw=src[0].rect.width;ih=src[0].rect.height;src.close()
        f=min(w/iw,h/ih);dw=iw*f;dh=ih*f
        rect=(x+(w-dw)/2,y-h+(h-dh)/2,dw,dh)
        if not hasattr(c,'vector_overlays'):c.vector_overlays=[]
        c.vector_overlays.append((str(vector),rect))
    else:
        iw,ih=Image.open(path).size;f=min(w/iw,h/ih);dw=iw*f;dh=ih*f
        c.drawImage(str(path),x+(w-dw)/2,y-h+(h-dh)/2,width=dw,height=dh,mask='auto')

def apply_vector_overlays(c,out,H):
    if not getattr(c,'vector_overlays',[]):return
    doc=fitz.open(out)
    for path,(x,y,w,h) in c.vector_overlays:
        src=fitz.open(path);doc[0].show_pdf_page(fitz.Rect(x,H-y-h,x+w,H-y),src,0);src.close()
    tmp=out.with_suffix('.vector.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(out)

def source_label(p):
    s=p.get('source',{}); short=s.get('commit','')[:12]
    return f"{s.get('repository','')}  |  {s.get('path','')}  |  {short}"

def intro_blocks(p,lang,scale=1):
    d=p['intro'][lang]; korean=lang=='ko';f='Korean' if korean else 'Sans';fb=f+'Bold'; title=d.get('title') if korean else p['title']; title=title or p['title']
    body=10.45*scale; lead=11.1*scale; titlefont=20.7*scale
    blocks=[('p',para(title,titlefont,fb,NAVY,leading=titlefont*1.23),9*scale),('p',para('이초록  |  KAIST' if korean else 'Chorok Lee  |  KAIST',9.8*scale,f,MUTED),12*scale),('p',para(d['hook'],lead,fb,SLATE,leading=lead*1.43),13*scale)]
    if p['id']=='icaif2026':
        edition='원본 TeX 기반 10쪽 프리프린트판 · 5쪽 제출본과 별도' if korean else 'Original ten-page TeX preprint edition; separate from the five-page submission.'
        blocks.insert(2,('p',para(edition,8.5*scale,f,MUTED,leading=11.8*scale),10*scale))
    for s in d.get('sections',[]):
        blocks += [('p',para(s['heading'],10.9*scale,fb,p.get('accent','#007F83'),leading=14.6*scale),3*scale),('p',para(s['text'],body,f,SLATE,leading=body*1.41),10*scale)]
    return blocks

def build_intro(p,lang,out):
    W,H=A4;m=44;w=W-2*m;d=p['intro'][lang];kor=lang=='ko';f='Korean' if kor else 'Sans';accent=p.get('accent','#007F83')
    footer_top=90; top=H-62
    takeaway_label='핵심 메시지' if kor else 'KEY TAKEAWAY'
    for scale in [1.12,1.08,1.04,1,.98,.96,.94,.92,.90,.88]:
        blocks=intro_blocks(p,lang,scale)
        take=para(d.get('takeaway',''),10.3*scale,f+'Bold',NAVY,leading=14.4*scale)
        take_h=ph(take,w-24)+39
        needed=sum(ph(b[1],w)+b[2] for b in blocks)+take_h
        if needed <= top-footer_top:break
    else: raise ValueError(f"Introduction too long: {p['id']}/{lang}, needs {needed:.1f}")
    c=canvas.Canvas(str(out),pagesize=A4,pageCompression=1)
    c.setTitle(f"{p['title']} - {'Korean' if kor else 'English'} introduction")
    c.setAuthor('Chorok Lee'); c.setSubject('One-page research introduction')
    c.setFillColor(colors.HexColor(accent));c.rect(m,H-38,34,3,fill=1,stroke=0)
    put(c,para('연구 소개' if kor else 'RESEARCH INTRODUCTION',8.4,f+'Bold',MUTED,leading=10),m+43,H-30,w-43)
    y=top
    for _,block,gap in blocks:y=put(c,block,m,y,w)-gap
    # Put take-away just after the body, with a soft band and colored rule.
    c.setFillColor(colors.HexColor(LIGHT)); c.rect(m,y-take_h,w,take_h,fill=1,stroke=0)
    c.setFillColor(colors.HexColor(accent));c.rect(m,y-take_h,3,take_h,fill=1,stroke=0)
    yy=put(c,para(takeaway_label,8.1*scale,f+'Bold',accent,leading=10),m+12,y-10,w-24)-5
    put(c,take,m+12,yy,w-24)
    line(c,m,73,w)
    footer='원문 및 코드' if kor else 'PAPER AND CODE'
    put(c,para(footer+'  |  '+p['source'].get('commit','')[:12],7.2,f+'Bold',MUTED,leading=9),m,65,w)
    repo=p['source'].get('repository','');url='https://github.com/'+repo
    put(c,para(repo,7.7,'Sans',MUTED,leading=10),m,52,w)
    c.linkURL(p['source'].get('url',url),(m,36,m+w,67),relative=0,thickness=0)
    c.showPage();c.save()
    mdtitle=d.get('title',p['title']) if kor else p['title']
    md=[f'# {mdtitle}','', '이초록 | KAIST' if kor else 'Chorok Lee | KAIST','',d['hook'],'']
    if p['id']=='icaif2026':
        md[4:4]=['원본 TeX 기반 10쪽 프리프린트판 · 5쪽 제출본과 별도' if kor else 'Original ten-page TeX preprint edition; separate from the five-page submission.','']
    for s in d['sections']:md += ['## '+s['heading'],'',s['text'],'']
    md += ['## '+takeaway_label,'',d.get('takeaway',''),'','Source: '+p['source'].get('url',url),'']
    out.with_suffix('.md').write_text('\n'.join(md))
    return {'paper':p['id'],'kind':'intro_'+lang,'scale':scale,'body_bottom':round(y-take_h,2),'footer_top':footer_top}

def make_table(d,w,size=34):
    headers=d['headers']; rows=d['rows'];n=len(headers)
    if n==2:widths=[w*.38,w*.62]
    elif n==3:widths=[w*.36,w*.32,w*.32]
    else:widths=[w/n]*n
    cells=[[para(x,size*.9,'SansBold',NAVY,leading=size*1.2) for x in headers]]+[[para(x,size,'Sans',SLATE,leading=size*1.3) for x in row] for row in rows]
    t=Table(cells,colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor(LIGHT)),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),18),('RIGHTPADDING',(0,0),(-1,-1),18),('TOPPADDING',(0,0),(-1,-1),16),('BOTTOMPADDING',(0,0),(-1,-1),17),('LINEBELOW',(0,0),(-1,0),2,colors.HexColor(RULE)),('LINEBELOW',(0,1),(-1,-1),1,colors.HexColor(RULE))]))
    return t

def poster_measure(p,scale):
    W,H=A0;m=112;w=W-2*m;g=72;cw=(w-g)/2;d=p['poster'];accent=p.get('accent','#007F83')
    poster_title=p['title'].replace(': ', ':\n',1) if p['id']=='icaif2026' else p['title']
    title=para(poster_title,70*scale,'SansBold',NAVY,leading=82*scale)
    hero=para(d['headline'],55*scale,'SansBold','#FFFFFF',leading=68*scale)
    question=para(d['question'],38*scale,'Sans',SLATE,leading=52*scale)
    sections=[]
    for s in d.get('sections',[]):sections.append((para(s['heading'],39*scale,'SansBold',accent,leading=49*scale),para(s['text'],34*scale,'Sans',SLATE,leading=46*scale)))
    rows=[]
    for i in range(0,len(sections),2):
        pair=sections[i:i+2]
        height=max(ph(a,cw)+15*scale+ph(b,cw) for a,b in pair)+42*scale
        rows.append((pair,height))
    table=make_table(d['table'],w,32*scale) if d.get('table') else None
    table_h=table.wrap(w,9999)[1] if table else 0
    figure_h=650*scale if d.get('figure') else 0
    caption=para(d['figure'].get('caption',''),24*scale,'Sans',MUTED,leading=33*scale) if d.get('figure') else None
    evidence_h=(58*scale+table_h+35*scale if table else 0)+(figure_h+ph(caption,w)+35*scale if figure_h else 0)
    # Conclusion and limitations always appear together, under the evidence.
    conc=para(d['conclusion'],38*scale,'SansBold',NAVY,leading=51*scale)
    limits=para(d['limitations'],30*scale,'Sans',SLATE,leading=41*scale)
    bottom_h=60*scale+ph(conc,w-58)+30*scale+ph(limits,w-58)+82*scale
    stats=d.get('key_numbers',[])
    stats_h=0
    if stats:
        sw=(w-45*(len(stats)-1))/len(stats)
        stats_h=max(ph(para(s['value'],62*scale,'SansBold',accent,leading=73*scale),sw)+ph(para(s['label'],27*scale,'Sans',SLATE,leading=37*scale),sw) for s in stats)+45*scale
    edition_h=43*scale if p['id']=='icaif2026' else 0
    header_h=ph(title,w)+87*scale+edition_h
    hero_h=ph(hero,w-76)+62*scale
    question_h=59*scale+ph(question,w)+42*scale
    total=header_h+hero_h+question_h+stats_h+sum(h for _,h in rows)+evidence_h+bottom_h+90
    return locals()

def build_poster(p,out):
    for scale in [1.18,1.15,1.12,1.09,1.06,1.03,1,.97,.94,.91,.88,.85,.82,.79]:
        q=poster_measure(p,scale)
        if q['total'] <= q['H']-2*q['m']:break
    else: raise ValueError(f"Poster overflow {p['id']}: {q['total']}")
    W,H,m,w,g,cw,d,accent=[q[k] for k in ['W','H','m','w','g','cw','d','accent']]
    c=canvas.Canvas(str(out),pagesize=A0,pageCompression=1)
    c.setTitle(p['title']+' - Research poster');c.setAuthor('Chorok Lee');c.setSubject('A0 portrait English research poster')
    c.setFillColor(colors.HexColor(accent));c.rect(0,H-21,W,21,fill=1,stroke=0)
    y=H-m
    y=put(c,q['title'],m,y,w)-23*scale
    y=put(c,para('CHOROK LEE   /   KAIST',29*scale,'SansBold',MUTED,leading=40*scale),m,y,w)-24*scale
    if p['id']=='icaif2026':
        y=put(c,para('Original ten-page TeX preprint edition; separate from the five-page submission.',23*scale,'Sans',MUTED,leading=31*scale),m,y,w)-12*scale
    c.setFillColor(colors.HexColor(NAVY));c.rect(m,y-q['hero_h'],w,q['hero_h'],fill=1,stroke=0)
    put(c,q['hero'],m+38,y-31*scale,w-76)
    y-=q['hero_h']+38*scale
    y=put(c,para('RESEARCH QUESTION',25*scale,'SansBold',accent,leading=32*scale),m,y,w)-13*scale
    y=put(c,q['question'],m,y,w)-42*scale
    stats=d.get('key_numbers',[])
    if stats:
        sw=(w-45*(len(stats)-1))/len(stats)
        for i,s in enumerate(stats):
            sx=m+i*(sw+45);sy=y
            sy=put(c,para(s['value'],62*scale,'SansBold',accent,leading=73*scale),sx,sy,sw)-7*scale
            put(c,para(s['label'],27*scale,'Sans',SLATE,leading=37*scale),sx,sy,sw)
        y-=q['stats_h'];line(c,m,y+15*scale,w);y-=15*scale
    for pair,h in q['rows']:
        for j,(head,body) in enumerate(pair):
            x=m+j*(cw+g);sy=put(c,head,x,y,cw)-15*scale;put(c,body,x,sy,cw)
        y-=h
    if q['table']:
        y=put(c,para('EVIDENCE AT A GLANCE',25*scale,'SansBold',accent,leading=34*scale),m,y,w)-24*scale
        q['table'].drawOn(c,m,y-q['table_h']);y-=q['table_h']+35*scale
    if d.get('figure'):
        fig=d['figure'];image_fit(c,fig['path'],m,y,w,q['figure_h'],fig.get('raster_only',False));y-=q['figure_h']
        y=put(c,q['caption'],m,y,w)-35*scale
    # Reserve a calm bottom band, expanding gap to use the A0 sheet well.
    y=min(y,H-m-q['total']+q['bottom_h']+90)
    y=max(y,q['bottom_h']+m+82)
    bottomtop=y
    c.setFillColor(colors.HexColor(LIGHT));c.rect(m,y-q['bottom_h'],w,q['bottom_h'],fill=1,stroke=0)
    c.setFillColor(colors.HexColor(accent));c.rect(m,y-q['bottom_h'],7,q['bottom_h'],fill=1,stroke=0)
    sy=put(c,para('TAKEAWAY',25*scale,'SansBold',accent,leading=32*scale),m+29,y-26*scale,w-58)-15*scale
    sy=put(c,q['conc'],m+29,sy,w-58)-25*scale
    sy=put(c,para('INTERPRETATION & LIMITS',23*scale,'SansBold',MUTED,leading=30*scale),m+29,sy,w-58)-11*scale
    sy=put(c,q['limits'],m+29,sy,w-58)
    line(c,m,m+37,w)
    put(c,para('PAPER & CODE  |  '+p['source'].get('repository',''),22*scale,'SansBold',MUTED,leading=29*scale),m,m+21,w)
    put(c,para('Source revision '+p['source'].get('commit','')[:12]+'  |  Research communication edition · 29 September 2026',18*scale,'Sans',MUTED,leading=24*scale),m,m-18,w)
    c.linkURL(p['source'].get('url','https://github.com/'+p['source']['repository']),(m,38,m+w,m+38),relative=0,thickness=0)
    c.showPage();c.save();apply_vector_overlays(c,out,H)
    return {'paper':p['id'],'kind':'poster','scale':scale,'measured':round(q['total'],1),'canvas_height':round(H,1),'bottom_band_top':round(bottomtop,1),'limits_bottom':round(sy,1)}

def render_preview(pdf,path,width=1400):
    doc=fitz.open(pdf)
    if len(doc)!=1:raise AssertionError(f'{pdf} has {len(doc)} pages')
    p=doc[0]
    subprocess.run(['/usr/bin/pdftoppm' if Path('/usr/bin/pdftoppm').exists() else 'pdftoppm','-singlefile','-scale-to-x',str(width),'-scale-to-y','-1','-png',str(pdf),str(path.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    try:
        with Image.open(path) as rendered: rendered.load()
        with Image.open(path) as rendered: rendered.verify()
    except (OSError,ValueError):
        # Some bundled Poppler builds report success but truncate PNGs; use MuPDF fallback.
        p.get_pixmap(matrix=fitz.Matrix(width/p.rect.width,width/p.rect.width),alpha=False).save(path)
    return {'pages':len(doc),'dimensions_pt':[round(p.rect.width,1),round(p.rect.height,1)],'characters':len(p.get_text())}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('ids',nargs='*');args=ap.parse_args()
    paths=[ROOT/'content'/f'{i}.json' for i in args.ids] if args.ids else sorted((ROOT/'content').glob('*.json'))
    report=[]
    for path in paths:
        p=json.loads(path.read_text());out=ROOT/'output'/p['id'];out.mkdir(parents=True,exist_ok=True);prev=ROOT/'qa'/p['id'];prev.mkdir(parents=True,exist_ok=True)
        for lang in ['en','ko']:
            pdf=out/f'introduction_{lang}.pdf';r=build_intro(p,lang,pdf);r.update(render_preview(pdf,prev/f'introduction_{lang}.png',1400));report.append(r)
        pdf=out/'poster_en.pdf';r=build_poster(p,pdf);r.update(render_preview(pdf,prev/'poster_en.png',1600));report.append(r)
    (ROOT/'qa').mkdir(exist_ok=True)
    metrics_path=ROOT/'qa'/'print_metrics.json'
    prior=json.loads(metrics_path.read_text()) if metrics_path.exists() else []
    merged={(x['paper'],x['kind']):x for x in prior}
    merged.update({(x['paper'],x['kind']):x for x in report})
    metrics_path.write_text(json.dumps([merged[k] for k in sorted(merged)],indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
