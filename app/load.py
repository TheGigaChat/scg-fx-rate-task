from __future__ import annotations

from pathlib import Path
from typing import Sequence, Tuple

TableRow = Tuple[str, str, str]


def build_exchange_rates_markdown(rows: Sequence[TableRow]) -> str:
    """Build markdown table for exchange rates output."""
    lines: list[str] = [
        "| Currency Code | Rate | Mean Historical Rate |",
        "|---|---:|---:|",
    ]
    for currency_code, rate, mean_historical_rate in rows:
        lines.append(
            f"| {currency_code} | {rate} | {mean_historical_rate} |"
        )
    return "\n".join(lines) + "\n"


def write_exchange_rates_markdown(output_path: Path, rows: Sequence[TableRow]) -> None:
    """Write exchange rates markdown table to a file."""
    markdown_content: str = build_exchange_rates_markdown(rows)
    output_path.write_text(markdown_content, encoding="utf-8")
