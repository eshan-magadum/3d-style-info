#!/usr/bin/env python3
"""OCR burned-in captions at 2 samples/second; this is not speech ASR."""
from pathlib import Path
import argparse, csv, re, subprocess, tempfile

p=argparse.ArgumentParser()
p.add_argument('--input',required=True)
p.add_argument('--out',required=True)
p.add_argument('--fps',type=float,default=2)
a=p.parse_args()
in_dir=Path(a.input); out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
rows=[]
for n,src in enumerate(sorted(in_dir.glob('*.mp4')),1):
    if 'Pasted text' in src.name: continue
    safe=re.sub(r'[^A-Za-z0-9_-]+','_',src.stem).strip('_')
    with tempfile.TemporaryDirectory(prefix='caption_ocr_') as td:
        td=Path(td)
        vf=f"fps={a.fps},crop=iw:ih*0.22:0:ih*0.76,scale=iw*3:-1,format=gray"
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(src),'-vf',vf,'-vsync','0',str(td/'f%06d.png')],check=True)
        imgs=sorted(td.glob('*.png'))
        for i,img in enumerate(imgs):
            r=subprocess.run(['tesseract',str(img),'stdout','--psm','7','-l','eng'],capture_output=True,text=True)
            text=' '.join(r.stdout.replace('\n',' ').split())
            rows.append({'clip_no':n,'clip':safe,'source':src.name,'time_s':round(i/a.fps,3),'text':text})
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['clip_no','clip','source','time_s','text']);w.writeheader();w.writerows(rows)
print(f'Wrote {len(rows)} timed caption samples to {out}')
