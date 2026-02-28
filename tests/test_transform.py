import unittest
from datetime import date

from app.transform import (
    compute_mean_historical_rates,
    format_rate,
    parse_daily_rates_latest,
    parse_historical_rates_series,
    validate_daily_against_historical_latest,
)


class TestTransform(unittest.TestCase):
    def test_parse_daily_rates_latest_success(self) -> None:
        csv_content = (
            "Date,USD,SEK,GBP,JPY\n"
            "2026-02-26,1.1000,10.5000,0.8500,180.00\n"
            "2026-02-27,1.2000,10.7000,0.8700,184.00\n"
        )

        latest_date, latest_rates = parse_daily_rates_latest(csv_content)

        self.assertEqual(latest_date, date(2026, 2, 27))
        self.assertEqual(latest_rates["USD"], 1.2)
        self.assertEqual(latest_rates["SEK"], 10.7)
        self.assertEqual(latest_rates["GBP"], 0.87)
        self.assertEqual(latest_rates["JPY"], 184.0)

    def test_parse_daily_rates_latest_missing_currency_value_raises(self) -> None:
        csv_content = "Date,USD,SEK,GBP,JPY\n2026-02-27,1.2000,,0.8700,184.00\n"

        with self.assertRaises(ValueError):
            parse_daily_rates_latest(csv_content)

    def test_parse_daily_rates_latest_invalid_numeric_value_raises(self) -> None:
        csv_content = "Date,USD,SEK,GBP,JPY\n2026-02-27,abc,10.7000,0.8700,184.00\n"

        with self.assertRaises(ValueError):
            parse_daily_rates_latest(csv_content)

    def test_parse_daily_rates_latest_no_valid_data_rows_raises(self) -> None:
        csv_content = "Date,USD,SEK,GBP,JPY\n"

        with self.assertRaises(ValueError):
            parse_daily_rates_latest(csv_content)

    def test_parse_historical_rates_series_success_and_skip_na(self) -> None:
        csv_content = (
            "Date,USD,SEK,GBP,JPY\n"
            "2026-02-27,1.2000,10.7000,0.8700,184.00\n"
            "2026-02-26,1.1000,N/A,0.8600,183.00\n"
        )

        series = parse_historical_rates_series(csv_content)

        self.assertEqual(len(series["USD"]), 2)
        self.assertEqual(len(series["SEK"]), 1)
        self.assertEqual(series["USD"][0], (date(2026, 2, 27), 1.2))

    def test_parse_historical_rates_series_no_valid_values_raises(self) -> None:
        csv_content = (
            "Date,USD,SEK,GBP,JPY\n"
            "2026-02-27,N/A,10.7000,0.8700,184.00\n"
        )

        with self.assertRaises(ValueError):
            parse_historical_rates_series(csv_content)

    def test_parse_historical_rates_series_invalid_numeric_raises(self) -> None:
        csv_content = "Date,USD,SEK,GBP,JPY\n2026-02-27,1.2000,10.7000,0.8700,bad\n"

        with self.assertRaises(ValueError):
            parse_historical_rates_series(csv_content)

    def test_compute_mean_historical_rates_success(self) -> None:
        series = {
            "USD": [(date(2026, 2, 27), 1.2), (date(2026, 2, 26), 1.0)],
            "SEK": [(date(2026, 2, 27), 10.0)],
        }

        means = compute_mean_historical_rates(series)

        self.assertAlmostEqual(means["USD"], 1.1)
        self.assertAlmostEqual(means["SEK"], 10.0)

    def test_compute_mean_historical_rates_empty_series_raises(self) -> None:
        series = {"USD": []}

        with self.assertRaises(ValueError):
            compute_mean_historical_rates(series)

    def test_format_rate_default_and_custom_decimals(self) -> None:
        self.assertEqual(format_rate(1.23456), "1.2346")
        self.assertEqual(format_rate(1.23456, decimals=2), "1.23")

    def test_validate_daily_against_historical_latest_success(self) -> None:
        latest_date = date(2026, 2, 27)
        latest_rates = {"USD": 1.2}
        historical_series = {"USD": [(date(2026, 2, 27), 1.2)]}

        validate_daily_against_historical_latest(
            latest_date, latest_rates, historical_series
        )

    def test_validate_daily_against_historical_latest_date_mismatch_raises(self) -> None:
        latest_date = date(2026, 2, 27)
        latest_rates = {"USD": 1.2}
        historical_series = {"USD": [(date(2026, 2, 26), 1.2)]}

        with self.assertRaises(ValueError):
            validate_daily_against_historical_latest(
                latest_date, latest_rates, historical_series
            )

    def test_validate_daily_against_historical_latest_rate_mismatch_raises(self) -> None:
        latest_date = date(2026, 2, 27)
        latest_rates = {"USD": 1.2}
        historical_series = {"USD": [(date(2026, 2, 27), 1.1)]}

        with self.assertRaises(ValueError):
            validate_daily_against_historical_latest(
                latest_date, latest_rates, historical_series
            )

    def test_validate_daily_against_historical_latest_missing_currency_raises(self) -> None:
        latest_date = date(2026, 2, 27)
        latest_rates = {"USD": 1.2}
        historical_series = {}

        with self.assertRaises(ValueError):
            validate_daily_against_historical_latest(
                latest_date, latest_rates, historical_series
            )


if __name__ == "__main__":
    unittest.main()
