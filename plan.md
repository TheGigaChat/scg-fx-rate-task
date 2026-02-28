# SEB FX ETL Task Plan

## Goal
Build a small Python 3.12+ ETL program that extracts ECB FX reference rates, transforms the data for selected currencies, and outputs a final table to `exchange_rates.md` (or `exchange_rates.html`) in the project root.

## Scope
- Input sources:
  - Daily rates ZIP: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip`
  - Historical rates ZIP: `https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip`
- Currencies to keep: `USD`, `SEK`, `GBP`, `JPY`
- Output columns:
  - `Currency Code`
  - `Rate`
  - `Mean Historical Rate`

## General Steps
1. Project setup
- Keep solution simple (`main.py` or a small module layout).
- Use explicit type hints for functions, variables, and return values.
- Add `README.md` with run instructions and output description.
- Add a separate AI-disclosure README as required by the assignment.

2. Extract
- Download/read both ECB ZIP endpoints.
- Open ZIP archives and load the XML payloads.
- Validate that required currency nodes are present.

3. Transform
- Parse daily rates and capture latest values for `USD`, `SEK`, `GBP`, `JPY`.
- Parse historical rates and collect full time-series values for those currencies.
- Compute mean historical rate per selected currency.
- Apply consistent numeric formatting/rounding for output.

4. Load
- Build a table with exactly 3 columns:
  - `Currency Code`, `Rate`, `Mean Historical Rate`.
- Write final result to `exchange_rates.md` at repo root.

5. Validation and polish
- Run end-to-end to confirm the file is generated without errors.
- Check that daily rate and historical mean are sourced correctly.
- If using external packages, freeze dependencies in `requirements.txt`.
- Ensure the repository is ready for submission (clean structure, clear docs).

## Acceptance Checklist
- Script runs from start to finish on Python 3.12+.
- Data is extracted from ECB daily and historical datasets (from local CSV files in `data/`).
- Only `USD`, `SEK`, `GBP`, `JPY` are included.
- Mean historical rates are correctly calculated.
- `exchange_rates.md` or `exchange_rates.html` exists in project root.
- README + AI usage disclosure are present.

## Completion Status (2026-02-28)
- Step 1 (Project setup): completed
- Step 2 (Extract): completed via provided local ECB CSV files in `data/`
- Step 3 (Transform): completed
- Step 4 (Load): completed (`exchange_rates.md`)
- Step 5 (Validation and polish): completed
