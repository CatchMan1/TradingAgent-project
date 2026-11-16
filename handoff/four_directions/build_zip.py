"""Validate manifest and build a source-only archive; run from any directory."""
from pathlib import Path
import hashlib,json,zipfile
P=Path(__file__).resolve().parent
m=json.loads((P/'manifest.json').read_text())
for item in m['files']:
 if hashlib.sha256((P/item['source']).read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Update reviewed manifest hash: '+item['source'])
z=P.parent/'TradingAgent-four-directions.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for f in sorted(P.rglob('*')):
  if not f.is_file() or any(part in {'__pycache__','.pytest_cache','.git'} for part in f.parts):continue
  if f.suffix not in {'.py','.md','.json','.csv','.txt'}:raise ValueError('Unexpected package file: '+str(f))
  out.write(f,'four_directions/'+str(f.relative_to(P)))
print(z, z.stat().st_size, 'bytes')
print('SHA256',hashlib.sha256(z.read_bytes()).hexdigest())
