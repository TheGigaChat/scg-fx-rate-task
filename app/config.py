from __future__ import annotations

from pathlib import Path

DATA_DIR: Path = Path("data")
DAILY_RATES_CSV_PATH: Path = DATA_DIR / "eurofxref.csv"
HISTORICAL_RATES_CSV_PATH: Path = DATA_DIR / "eurofxref-hist.csv"
OUTPUT_MARKDOWN_PATH: Path = Path("exchange_rates.md")
