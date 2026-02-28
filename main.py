from pathlib import Path

from app.transform import parse_daily_rates_latest


def main() -> None:
    daily_csv_path: Path = Path("data/eurofxref.csv")
    latest_date, latest_rates = parse_daily_rates_latest(daily_csv_path)

    print(f"Latest daily rates date: {latest_date.isoformat()}")
    for currency_code, rate in latest_rates.items():
        print(f"{currency_code}: {rate}")


if __name__ == "__main__":
    main()
