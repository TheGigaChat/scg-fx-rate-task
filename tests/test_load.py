import tempfile
import unittest
from pathlib import Path

from app.load import build_exchange_rates_markdown, write_exchange_rates_markdown


class TestLoad(unittest.TestCase):
    def test_build_exchange_rates_markdown_exact_structure(self) -> None:
        rows = [
            ("USD", "1.1805", "1.1823"),
            ("SEK", "10.6643", "9.6907"),
        ]

        markdown = build_exchange_rates_markdown(rows)

        expected = (
            "| Currency Code | Rate | Mean Historical Rate |\n"
            "|---|---:|---:|\n"
            "| USD | 1.1805 | 1.1823 |\n"
            "| SEK | 10.6643 | 9.6907 |\n"
        )
        self.assertEqual(markdown, expected)
        self.assertTrue(markdown.endswith("\n"))

    def test_write_exchange_rates_markdown_writes_file(self) -> None:
        rows = [("GBP", "0.8763", "0.7849")]

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "exchange_rates.md"
            write_exchange_rates_markdown(output_path, rows)

            self.assertTrue(output_path.exists())
            content = output_path.read_text(encoding="utf-8")
            self.assertIn("| GBP | 0.8763 | 0.7849 |", content)


if __name__ == "__main__":
    unittest.main()
