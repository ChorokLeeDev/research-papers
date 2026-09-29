from pathlib import Path
import ast
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
import json
root=Path(__file__).resolve().parent
data=json.loads((root/'concentration_evidence_data.json').read_text())['data']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,ax=plt.subplots(figsize=(10.6,6.25),facecolor='white')
for k,c,m,label in [('salt_tasks','#2563A6','o','8 SALT tasks'),('ext_tasks','#C46625','^','8 external tasks')]:
 vals=data[k];ax.scatter([v[1] for v in vals],[v[2] for v in vals],s=110,color=c,marker=m,label=label,zorder=4,edgecolor='white',linewidth=.8)
ax.axvline(40,color='#64748B',ls='--',lw=1.3)
ax.text(39.0,33,'40% exploratory cutoff',rotation=90,va='center',ha='right',fontsize=11,color='#64748B')
lookup={v[0]:v for vals in data.values() for v in vals}
for name,xytext in [('Covertype',(34,88)),('s-payterms',(55,88)),('s-office',(48,7)),('KDDCup99',(8,27))]:
 _,x,y=lookup[name];color='#2563A6' if name.startswith('s-') else '#C46625';ax.annotate(name,(x,y),xytext=xytext,textcoords='data',fontsize=12.5,color=color,arrowprops={'arrowstyle':'-','color':color,'lw':.85},ha='left')
ax.text(.035,.94,'Spearman ρ = 0.853\nn = 16 tasks · 9 domains',transform=ax.transAxes,va='top',fontsize=15,color='#172B4D')
ax.set(xlim=(0,65),ylim=(-8,95),xlabel='Validation-time top-1 SHAP concentration (%)',ylabel='Coverage loss (percentage points)')
ax.set_xticks([0,10,20,30,40,50,60]);ax.set_yticks([0,20,40,60,80]);ax.grid(axis='y',alpha=.2,zorder=0);ax.set_axisbelow(True)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.17),ncol=2,frameon=False,fontsize=12)
fig.subplots_adjust(left=.11,right=.98,top=.98,bottom=.21)
for ext in ['png','svg','pdf']:
 fig.savefig(root/f'concentration_evidence.{ext}',dpi=190,facecolor='white')
print('Replotted exact source-script values; Spearman =',spearmanr([v[1] for a in data.values() for v in a],[v[2] for a in data.values() for v in a]).statistic)
