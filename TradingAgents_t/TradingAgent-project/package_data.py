"""将当前 data/ 单独打包，供 GitHub Release 分享；不修改原始数据。"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib

ROOT = Path(__file__).resolve().parent


def package_data():
    data_dir = ROOT / "data"
    for name in ["sources.json", "prices", "financials", "raw"]:
        if not (data_dir / name).exists():
            raise FileNotFoundError(f"缺少数据：{name}，请先下载数据包或完成采集")
    files = [data_dir / "sources.json"]
    for name in ["prices", "financials", "raw", "decisions"]:
        files.extend(path for path in (data_dir / name).rglob("*")
                     if path.is_file() and not any(part.startswith(".") for part in path.relative_to(data_dir).parts))
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    archive = output / "trading-data.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as zipped:
        for path in sorted(files):
            zipped.write(path, path.relative_to(ROOT))
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / "trading-data.zip.sha256").write_text(f"{checksum}  {archive.name}\n")
    print(f"{archive.name}: {len(files)} files, {archive.stat().st_size / 1024**2:.2f} MB")
    return archive


if __name__ == "__main__":
    package_data()
