from pathlib import Path

from app.config import DAILY_RATES_CSV_PATH, HISTORICAL_RATES_CSV_PATH, OUTPUT_MARKDOWN_PATH
from app.load import write_exchange_rates_markdown
from app.transform import (
    TARGET_CURRENCIES,
    compute_mean_historical_rates,
    format_rate,
    parse_daily_rates_latest,
    parse_historical_rates_series,
    validate_daily_against_historical_latest,
)


def main() -> None:
    daily_csv_path: Path = DAILY_RATES_CSV_PATH
    historical_csv_path: Path = HISTORICAL_RATES_CSV_PATH
    output_markdown_path: Path = OUTPUT_MARKDOWN_PATH
    latest_date, latest_rates = parse_daily_rates_latest(daily_csv_path)
    historical_series = parse_historical_rates_series(historical_csv_path)
    validate_daily_against_historical_latest(latest_date, latest_rates, historical_series)
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

    table_rows: list[tuple[str, str, str]] = []
    for currency_code in TARGET_CURRENCIES:
        daily_rate = format_rate(latest_rates[currency_code])
        mean_rate = format_rate(mean_historical_rates[currency_code])
        table_rows.append((currency_code, daily_rate, mean_rate))
        row: str = (
            f"{currency_code:<{col_currency}} | "
            f"{daily_rate:>{col_rate}} | "
            f"{mean_rate:>{col_mean}}"
        )
        print(row)

    write_exchange_rates_markdown(output_markdown_path, table_rows)
    print(f"\nSaved markdown output to: {output_markdown_path}")
    print("Validation check: daily rates match latest historical points.")


if __name__ == "__main__":
    main()
