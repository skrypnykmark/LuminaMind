"""
Utility script to download and unpack the ML models.

Usage (from repo root or ml/ directory):

    cd ml
    python download_models.py

Edit the MODEL_URLS below to point to your hosted zip files
for the mood and risk models.
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path
from urllib.request import urlopen


BASE = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE / "models"

# TODO: replace these with your real URLs
MODEL_URLS = {
    "mood4_model": "https://drive.google.com/uc?export=download&id=1ky23-XrfHXg7Kd87XGvzCZQxC2HiW_hn" ,
    "risk_model": "https://drive.google.com/uc?export=download&id=1duHGX6Jeb_ZD2trB4gOx5tOP3BqatxGi",
}


def download_and_extract(name: str, url: str) -> None:
    target_dir = MODELS_DIR / name
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {name} from {url} ...")
    with urlopen(url) as resp:
        data = resp.read()

    print(f"Unpacking into {target_dir} ...")
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        zf.extractall(target_dir)

    print(f"Done: {name}")


def main() -> None:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    for name, url in MODEL_URLS.items():
        if "your-storage.example.com" in url:
            print(
                f"Skip {name}: please edit MODEL_URLS in download_models.py "
                "to point to your actual zip URL."
            )
            continue

        download_and_extract(name, url)


if __name__ == "__main__":
    main()

