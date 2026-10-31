"""Regenerate conservative review PNGs from preserved references; never alters approved originals.
Python 3.10+, Pillow and NumPy. Usage: python logos/working/build_package.py
For comparison/layout rebuild use original v0.1.0 proof as reference; PDF is not regenerated here.
"""
from pathlib import Path
import argparse
from PIL import Image, ImageDraw
import numpy as np
p=argparse.ArgumentParser(description=__doc__);p.parse_args()
root=Path(__file__).resolve().parents[2]
for f in (root/'logos/approved').glob('*.png'):
 im=Image.open(f).convert('RGB');a=np.array(im);e=(a.min(2)>180)&((a.max(2)-a.min(2))<65)
 m=Image.fromarray(np.uint8(e)*255).convert('RGB')
 for xy in [(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)]:
  if m.getpixel(xy)==(255,255,255):ImageDraw.floodfill(m,xy,(255,0,0),thresh=0)
 out=Image.fromarray(np.dstack([a,np.where(np.all(np.array(m)==[255,0,0],2),0,255).astype('uint8')]))
 out=out.crop(out.getbbox());name=f.stem.removeprefix('ama-')
 out.save(root/f'logos/review/AMA_Logo_{name}_{out.width}x{out.height}_EN_v001_REVIEW.png')
print('Review cutouts regenerated. Inspect edges manually; no production approval implied.')
