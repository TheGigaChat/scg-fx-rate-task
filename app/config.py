from __future__ import annotations

from pathlib import Path

DAILY_RATES_ZIP_URL: str = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip"
HISTORICAL_RATES_ZIP_URL: str = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip"
OUTPUT_MARKDOWN_PATH: Path = Path("exchange_rates.md")
