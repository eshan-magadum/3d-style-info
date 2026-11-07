#!/usr/bin/env python3
"""Plot selected per-frame measurements; camera shift remains only a proxy."""
from pathlib import Path
import argparse,csv,json
import numpy as np
import matplotlib.pyplot as plt

p=argparse.ArgumentParser();p.add_argument('--csv',required=True);p.add_argument('--manifest',required=True);p.add_argument('--out',required=True);a=p.parse_args()
rows={}
with open(a.csv,encoding='utf-8',newline='') as f:
 for r in csv.DictReader(f): rows.setdefault(r['clip_id'],[]).append(r)
manifest=json.load(open(a.manifest,encoding='utf-8'))
fig,axs=plt.subplots(4,1,figsize=(13,13),sharex=True,constrained_layout=True)
colors=['#1976d2','#e65100','#2e7d32','#6a1b9a','#00838f']
for i,clip in enumerate(manifest['clips']):
 cid=clip['clip_id']; rr=rows[cid]; dur=clip['duration_s']; t=np.array([float(x['time_s'])/dur for x in rr]); color=colors[i]
 def smooth(key):
  x=np.array([float(r[key]) for r in rr]); n=30
  return np.convolve(x,np.ones(n)/n,mode='same')
 label=f"{i+1:02d} {cid.split('_',1)[1].replace('_',' ')}"
 axs[0].plot(t,smooth('luma_mean'),lw=1.0,color=color,label=label)
 axs[1].plot(t,smooth('saturation_mean'),lw=1.0,color=color)
 axs[2].plot(t,smooth('contrast_p90_p10'),lw=1.0,color=color)
 dx=np.array([float(r['phase_image_dx_px']) for r in rr]);dy=np.array([float(r['phase_image_dy_px']) for r in rr]);mag=np.hypot(dx,dy)
 axs[3].plot(t,np.convolve(mag,np.ones(30)/30,mode='same'),lw=1.0,color=color)
axs[0].set_ylabel('Mean luma');axs[1].set_ylabel('Mean saturation');axs[2].set_ylabel('Luma contrast\n(p90 − p10)');axs[3].set_ylabel('Phase-correlation\nshift proxy (px/frame)');axs[3].set_xlabel('Normalized clip progress')
for ax in axs: ax.grid(True,alpha=.25);ax.set_xlim(0,1)
axs[0].legend(loc='upper left',fontsize=8,ncol=2,framealpha=.9)
fig.suptitle('Five reference shorts — frame metrics smoothed over 1 second',fontsize=14)
Path(a.out).parent.mkdir(parents=True,exist_ok=True);fig.savefig(a.out,dpi=160);print(a.out)
