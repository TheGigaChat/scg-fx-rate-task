from pathlib import Path

from app.transform import (
    compute_mean_historical_rates,
    format_rate,
    parse_daily_rates_latest,
    parse_historical_rates_series,
)


def main() -> None:
    daily_csv_path: Path = Path("data/eurofxref.csv")
    historical_csv_path: Path = Path("data/eurofxref-hist.csv")
    latest_date, latest_rates = parse_daily_rates_latest(daily_csv_path)
    historical_series = parse_historical_rates_series(historical_csv_path)
    mean_historical_rates = compute_mean_historical_rates(historical_series)

    col_currency: int = 13
    col_rate: int = 10
    col_mean: int = 20

    print(f"Latest daily rates date: {latest_date.isoformat()}\n")
    header: str = (
        f"{'Currency Code':<{col_currency}} | "
        f"{'Rate':>{col_rate}} | "
        f"{'Mean Historical Rate':>{col_mean}}"
    )
    separator: str = "-" * len(header)
    print(header)
    print(separator)

    for currency_code in latest_rates:
        daily_rate = format_rate(latest_rates[currency_code])
        mean_rate = format_rate(mean_historical_rates[currency_code])
        row: str = (
            f"{currency_code:<{col_currency}} | "
            f"{daily_rate:>{col_rate}} | "
            f"{mean_rate:>{col_mean}}"
        )
        print(row)


if __name__ == "__main__":
    main()
