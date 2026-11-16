"""Preview/install the complete source overlay. No model/network calls."""
import argparse,hashlib,json,shutil
from pathlib import Path
from datetime import datetime,timezone

def install(destination,apply=False):
 root=Path(__file__).resolve().parent;dest=Path(destination).resolve()
 if not (dest/'framework/tradingagents').is_dir():raise ValueError('Destination must be an existing TradingAgent-project checkout')
 manifest=json.loads((root/'manifest.json').read_text());planned=[]
 for item in manifest['files']:
  source=(root/item['source']).resolve();target=(dest/item['destination']).resolve()
  if not source.is_relative_to(root) or not target.is_relative_to(dest):raise ValueError('Path escapes package/project')
  if hashlib.sha256(source.read_bytes()).hexdigest()!=item['sha256']:raise ValueError('Manifest mismatch: '+item['source'])
  if target.exists() and target.read_bytes()==source.read_bytes():continue
  planned.append((source,target,item['destination']))
 print(json.dumps({'apply':apply,'base_commit':manifest['base_commit'],'changes':[rel for _,_,rel in planned]},indent=2))
 if not apply:return
 backup=dest/'handoff-backups'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
 for source,target,rel in planned:
  if target.exists():
   saved=backup/rel;saved.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,saved)
  target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
 print('Applied. Existing files backed up under',backup)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--destination',required=True);p.add_argument('--apply',action='store_true');a=p.parse_args();install(a.destination,a.apply)
