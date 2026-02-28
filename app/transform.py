from __future__ import annotations

import csv
from datetime import date, datetime
from pathlib import Path
from typing import Dict, Sequence, Tuple

TARGET_CURRENCIES: tuple[str, ...] = ("USD", "SEK", "GBP", "JPY")


def _parse_ecb_date(value: str) -> date:
    """Parse date formats used by ECB CSV files."""
    date_formats: tuple[str, ...] = ("%d %B %Y", "%Y-%m-%d")
    for date_format in date_formats:
        try:
            return datetime.strptime(value.strip(), date_format).date()
        except ValueError:
            continue
    raise ValueError(f"Unsupported date format: '{value}'.")


def parse_daily_rates_latest(
    csv_path: Path, currencies: Sequence[str] = TARGET_CURRENCIES
) -> Tuple[date, Dict[str, float]]:
    """
    Parse the daily rates CSV and capture latest values for requested currencies.
    """
    latest_date: date | None = None
    latest_rates: Dict[str, float] = {}

    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        if not reader.fieldnames:
            raise ValueError("Daily rates CSV has no headers.")

        for row in reader:
            normalized_row: Dict[str, str] = {
                (key or "").strip(): (value or "").strip()
                for key, value in row.items()
            }
            raw_date: str = normalized_row.get("Date", "")
            if not raw_date:
                continue

            row_date: date = _parse_ecb_date(raw_date)
            if latest_date is not None and row_date <= latest_date:
                continue

            row_rates: Dict[str, float] = {}
            for currency in currencies:
                raw_value: str = normalized_row.get(currency, "")
                if not raw_value or raw_value == "N/A":
                    raise ValueError(
                        f"Missing daily rate for currency '{currency}' on {row_date}."
                    )
                try:
                    row_rates[currency] = float(raw_value)
                except ValueError as error:
                    raise ValueError(
                        f"Invalid daily rate '{raw_value}' for currency '{currency}' on {row_date}."
                    ) from error

            latest_date = row_date
            latest_rates = row_rates

    if latest_date is None:
        raise ValueError("Daily rates CSV contains no valid data rows.")

    return latest_date, latest_rates
