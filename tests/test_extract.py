import unittest
from io import BytesIO
from unittest.mock import Mock, patch
from zipfile import ZipFile

from app import extract


class TestExtract(unittest.TestCase):
    @staticmethod
    def _build_zip_bytes(file_name: str, file_content: str) -> bytes:
        buffer = BytesIO()
        with ZipFile(buffer, "w") as zip_file:
            zip_file.writestr(file_name, file_content.encode("utf-8"))
        return buffer.getvalue()

    def test_download_csv_from_zip_url_success(self) -> None:
        zip_bytes = self._build_zip_bytes("rates.csv", "Date,USD\n2026-02-27,1.2\n")

        mock_response = Mock()
        mock_response.read.return_value = zip_bytes
        mock_context = Mock()
        mock_context.__enter__ = Mock(return_value=mock_response)
        mock_context.__exit__ = Mock(return_value=None)

        with patch("app.extract.urlopen", return_value=mock_context):
            csv_text = extract.download_csv_from_zip_url("https://example.com/test.zip")

        self.assertIn("Date,USD", csv_text)
        self.assertIn("2026-02-27,1.2", csv_text)

    def test_download_csv_from_zip_url_no_csv_raises(self) -> None:
        zip_bytes = self._build_zip_bytes("rates.txt", "not csv")

        mock_response = Mock()
        mock_response.read.return_value = zip_bytes
        mock_context = Mock()
        mock_context.__enter__ = Mock(return_value=mock_response)
        mock_context.__exit__ = Mock(return_value=None)

        with patch("app.extract.urlopen", return_value=mock_context):
            with self.assertRaises(ValueError):
                extract.download_csv_from_zip_url("https://example.com/test.zip")

    def test_extract_ecb_csv_contents_calls_both_urls(self) -> None:
        side_effect_results = ["daily_csv", "historical_csv"]
        with patch(
            "app.extract.download_csv_from_zip_url", side_effect=side_effect_results
        ) as mocked_download:
            daily, historical = extract.extract_ecb_csv_contents()

        self.assertEqual(daily, "daily_csv")
        self.assertEqual(historical, "historical_csv")
        self.assertEqual(mocked_download.call_count, 2)
        first_call_url = mocked_download.call_args_list[0].args[0]
        second_call_url = mocked_download.call_args_list[1].args[0]
        self.assertEqual(first_call_url, extract.DAILY_RATES_ZIP_URL)
        self.assertEqual(second_call_url, extract.HISTORICAL_RATES_ZIP_URL)


if __name__ == "__main__":
    unittest.main()
