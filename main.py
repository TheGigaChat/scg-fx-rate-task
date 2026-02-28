from pathlib import Path

from app.transform import parse_daily_rates_latest, parse_historical_rates_series


def main() -> None:
    daily_csv_path: Path = Path("data/eurofxref.csv")
    historical_csv_path: Path = Path("data/eurofxref-hist.csv")
    latest_date, latest_rates = parse_daily_rates_latest(daily_csv_path)
    historical_series = parse_historical_rates_series(historical_csv_path)

    print(f"Latest daily rates date: {latest_date.isoformat()}")
    for currency_code, rate in latest_rates.items():
        print(f"{currency_code}: {rate}")

    print("\nHistorical series summary:")
    for currency_code, values in historical_series.items():
        latest_hist_date, latest_hist_rate = values[0]
        print(
            f"{currency_code}: {len(values)} values, "
            f"latest historical point {latest_hist_date.isoformat()} -> {latest_hist_rate}"
        )


if __name__ == "__main__":
    main()
