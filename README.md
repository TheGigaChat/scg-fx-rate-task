# SEB FX ETL Task

Small Python ETL solution for ECB euro foreign exchange reference rates.

## What This Script Does
- Reads daily rates from `data/eurofxref.csv`
- Reads historical rates from `data/eurofxref-hist.csv`
- Keeps only `USD`, `SEK`, `GBP`, `JPY`
- Computes mean historical rate for each selected currency
- Writes final markdown table to `exchange_rates.md`

## Project Structure
- `main.py`: ETL entry point
- `app/transform.py`: parsing, validation, and transform logic
- `app/load.py`: markdown table generation and file writing
- `app/config.py`: file path configuration
- `data/`: input CSV files
- `exchange_rates.md`: generated output

## Requirements
- Python 3.12+ recommended by assignment (works with standard library only)
- No external packages are required

## Run
```bash
python main.py
```

## Output
Running the script generates `exchange_rates.md` in the project root with columns:
- `Currency Code`
- `Rate`
- `Mean Historical Rate`

## Validation Included
The script checks that daily rates match the latest date/rate points from historical data for each selected currency.

## AI Usage Disclosure
AI usage and prompt logs are documented in:
- `README_AI.md`
- `prompts.md`
