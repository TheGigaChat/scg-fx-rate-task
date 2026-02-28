from __future__ import annotations

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from app.config import DAILY_RATES_ZIP_URL, HISTORICAL_RATES_ZIP_URL


def download_csv_from_zip_url(zip_url: str, timeout_seconds: int = 30) -> str:
    """Download a ZIP file from URL and return the first CSV file content as text."""
    with urlopen(zip_url, timeout=timeout_seconds) as response:
        zip_bytes: bytes = response.read()

    with ZipFile(BytesIO(zip_bytes)) as zip_file:
        csv_names: list[str] = [
            name for name in zip_file.namelist() if name.lower().endswith(".csv")
        ]
        if not csv_names:
            raise ValueError(f"No CSV file found inside ZIP from '{zip_url}'.")

        csv_name: str = sorted(csv_names)[0]
        with zip_file.open(csv_name) as csv_file:
            csv_bytes: bytes = csv_file.read()

    return csv_bytes.decode("utf-8-sig")


def extract_ecb_csv_contents() -> tuple[str, str]:
    """Download and return daily and historical ECB CSV contents in memory."""
    daily_csv_content: str = download_csv_from_zip_url(DAILY_RATES_ZIP_URL)
    historical_csv_content: str = download_csv_from_zip_url(HISTORICAL_RATES_ZIP_URL)
    return daily_csv_content, historical_csv_content
