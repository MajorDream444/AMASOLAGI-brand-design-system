from pathlib import Path
import csv,re,hashlib,xml.etree.ElementTree as E
from PIL import Image
p=Path(__file__).resolve().parents[2]
rows=list(csv.DictReader((p/'brand/ASSET_REGISTER.csv').open()))
assert len({r['asset_id'] for r in rows})==len(rows)
assert len({r['path'] for r in rows})==len(rows)
for r in rows: assert (p/r['path']).is_file(),r['path']
for f in p.rglob('*.svg'): E.parse(f)
for f in (p/'logos/review').glob('*.png'):
 im=Image.open(f);assert im.mode=='RGBA';assert im.getextrema()[3][0]==0
 m=re.search(r'_(\d+)x(\d+)_',f.name)
 if m: assert im.size==(int(m[1]),int(m[2])),f.name
for f in (p/'logos/approved').glob('*.png'):
 src=p/'logos/sources/supplied-package/02-Logo-Masters/approved-raster'/f.name
 assert f.read_bytes()==src.read_bytes()
print('PASS: register paths/IDs, SVG XML, PNG dimensions/alpha, byte-identical approved copies')
