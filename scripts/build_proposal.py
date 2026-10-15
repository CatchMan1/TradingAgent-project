from pathlib import Path
from html import escape
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Drawing, Rect, Line, Polygon, String
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]
out=root/'output/pdf'
out.mkdir(parents=True,exist_ok=True)
styles={
 'title':ParagraphStyle('title',fontName='Helvetica-Bold',fontSize=13,leading=15,spaceAfter=5),
 'meta':ParagraphStyle('meta',fontName='Helvetica',fontSize=9,leading=11,spaceAfter=2),
 'heading':ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=10.5,leading=12,spaceBefore=6,spaceAfter=3),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=9.5,leading=11.3,spaceAfter=4,alignment=TA_LEFT),
 'refs':ParagraphStyle('refs',fontName='Helvetica',fontSize=8,leading=9.5,spaceAfter=0),
}
def markup(s):
 s=escape(s)
 return re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)

def framework():
 w=A4[0]-68
 d=Drawing(w,128)
 ink=colors.HexColor('#294457')
 def box(x,y,bw,bh,lines,fill='#EFF5F9'):
  d.add(Rect(x,y,bw,bh,rx=3,ry=3,fillColor=colors.HexColor(fill),strokeColor=colors.HexColor('#9BAFBE'),strokeWidth=.6))
  for i,t in enumerate(lines):
   d.add(String(x+bw/2,y+bh/2+(len(lines)-1)*4-i*8-2.3,t,fontName='Helvetica',fontSize=7.2,textAnchor='middle',fillColor=ink))
 def arrow(x1,y1,x2,y2):
  d.add(Line(x1,y1,x2,y2,strokeColor=ink,strokeWidth=.7))
  if y1==y2:
   pts=[x2,y2,x2-3.6,y2+2,x2-3.6,y2-2]
  else:
   pts=[x2,y2,x2-2,y2+3.6,x2+2,y2+3.6]
  d.add(Polygon(pts,fillColor=ink,strokeColor=None))
 box(0,105,w,17,['Historical prices / indicators  |  SEC facts  |  timestamped news (filtered by decision cutoff)'])
 gap=10
 aw=(w-3*gap)/4
 for i,label in enumerate(['Technical analyst','Fundamental analyst','News analyst','News-sentiment analyst']):
  x=i*(aw+gap)
  box(x,73,aw,22,[label], '#E8F1F8')
  arrow(x+aw/2,105,x+aw/2,95)
  d.add(Line(x+aw/2,73,x+aw/2,59,strokeColor=ink,strokeWidth=.7))
 d.add(Line(aw/2,59,3*(aw+gap)+aw/2,59,strokeColor=ink,strokeWidth=.7))
 widths=[125,62,105,92,w-125-62-105-92-48]
 labels=[['Bull / bear debate','+ research manager'],['Trader','proposal'],['Risk discussion','(risk perspectives)'],['Final manager','rating'],['Position mapping','next-open backtest']]
 x=0
 for i,(bw,ls) in enumerate(zip(widths,labels)):
  box(x,19,bw,29,ls,'#F2F5EF' if i==4 else '#EFF5F9')
  if i==0:arrow(bw/2,59,bw/2,48)
  if i<4:arrow(x+bw,33.5,x+bw+12,33.5)
  x+=bw+12
 d.add(String(0,4,'Figure 1. Proposed workflow. News and sentiment roles share historical news inputs.',fontName='Helvetica-Oblique',fontSize=7.4,fillColor=ink))
 return d
text=(root/'proposal.md').read_text()
story=[]
for block in text.split('\n\n'):
 block=block.strip()
 if not block:continue
 if block.startswith('<!-- FRAMEWORK_FIGURE'):
  story.append(framework())
 elif block.startswith('```mermaid') or block.startswith('*Figure 1.'):
  continue
 elif block.startswith('# '):
  story.append(Paragraph(markup(block[2:]),styles['title']))
 elif block.startswith('## '):
  story.append(Paragraph(markup(block[3:]),styles['heading']))
 elif block.startswith('**MSBD'):
  for line in block.splitlines():story.append(Paragraph(markup(line.strip()),styles['meta']))
 elif block.startswith('**References:'):
  story.append(Paragraph(markup(block),styles['refs']))
 else:story.append(Paragraph(markup(block.replace('\n',' ')),styles['body']))
p=out/'MSBD5018_Proposal_Submission.pdf'
doc=SimpleDocTemplate(str(p),pagesize=A4,leftMargin=34,rightMargin=34,topMargin=30,bottomMargin=28,
 title='Evaluating Multi-Agent Collaboration in LLM-Based Trading',author='MSBD 5018 Project Team')
doc.build(story)
n=len(PdfReader(p).pages)
print(f'{p}: {n} pages')
if n!=1:raise SystemExit('Proposal must be exactly one page')
