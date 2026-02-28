from __future__ import annotations

import csv
from datetime import date, datetime
from io import StringIO
from typing import Dict, List, Sequence, Tuple

TARGET_CURRENCIES: tuple[str, ...] = ("USD", "SEK", "GBP", "JPY")
RateSeries = Dict[str, List[Tuple[date, float]]]
DEFAULT_DECIMALS: int = 4


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
    csv_content: str, currencies: Sequence[str] = TARGET_CURRENCIES
) -> Tuple[date, Dict[str, float]]:
    """
    Parse the daily rates CSV and capture latest values for requested currencies.
    """
    latest_date: date | None = None
    latest_rates: Dict[str, float] = {}

    with StringIO(csv_content) as file:
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


def parse_historical_rates_series(
    csv_content: str, currencies: Sequence[str] = TARGET_CURRENCIES
) -> RateSeries:
    """
    Parse historical rates CSV and collect full time-series for requested currencies.
    """
    series_by_currency: RateSeries = {currency: [] for currency in currencies}

    with StringIO(csv_content) as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        if not reader.fieldnames:
            raise ValueError("Historical rates CSV has no headers.")

        for row in reader:
            normalized_row: Dict[str, str] = {
                (key or "").strip(): (value or "").strip()
                for key, value in row.items()
            }
            raw_date: str = normalized_row.get("Date", "")
            if not raw_date:
                continue

            row_date: date = _parse_ecb_date(raw_date)
            for currency in currencies:
                raw_value: str = normalized_row.get(currency, "")
                if not raw_value or raw_value == "N/A":
                    continue
                try:
                    rate: float = float(raw_value)
                except ValueError as error:
                    raise ValueError(
                        f"Invalid historical rate '{raw_value}' for currency '{currency}' on {row_date}."
                    ) from error
                series_by_currency[currency].append((row_date, rate))

    missing_currencies: List[str] = [
        currency for currency, values in series_by_currency.items() if not values
    ]
    if missing_currencies:
        missing_list: str = ", ".join(missing_currencies)
        raise ValueError(
            f"Historical rates CSV has no valid values for: {missing_list}."
        )

    return series_by_currency


def compute_mean_historical_rates(series_by_currency: RateSeries) -> Dict[str, float]:
    """Compute arithmetic mean historical rate for each currency."""
    mean_by_currency: Dict[str, float] = {}

    for currency, values in series_by_currency.items():
        if not values:
            raise ValueError(f"Cannot compute mean for '{currency}' with no values.")

        total: float = sum(rate for _, rate in values)
        mean_by_currency[currency] = total / len(values)

    return mean_by_currency


def format_rate(value: float, decimals: int = DEFAULT_DECIMALS) -> str:
    """Format numeric rate with consistent rounding."""
    return f"{value:.{decimals}f}"


def validate_daily_against_historical_latest(
    latest_date: date,
    latest_rates: Dict[str, float],
    historical_series: RateSeries,
    tolerance: float = 1e-9,
) -> None:
    """
    Validate that daily rates match the latest point in historical series.
    """
    for currency, daily_rate in latest_rates.items():
        historical_values: List[Tuple[date, float]] = historical_series.get(currency, [])
        if not historical_values:
            raise ValueError(
                f"Missing historical series for currency '{currency}'."
            )

        historical_latest_date, historical_latest_rate = max(
            historical_values, key=lambda point: point[0]
        )
        if historical_latest_date != latest_date:
            raise ValueError(
                f"Date mismatch for '{currency}': daily={latest_date}, "
                f"historical latest={historical_latest_date}."
            )

        if abs(historical_latest_rate - daily_rate) > tolerance:
            raise ValueError(
                f"Rate mismatch for '{currency}' on {latest_date}: "
                f"daily={daily_rate}, historical={historical_latest_rate}."
            )
