# AI Memory Bank

## Project Overview
This repository contains a small Python ETL assignment based on ECB euro foreign exchange reference rates.

Main objective:
- Extract daily and historical FX data
- Transform data for selected currencies (`USD`, `SEK`, `GBP`, `JPY`)
- Compute mean historical rate for each selected currency
- Load final result into `exchange_rates.md` (or `exchange_rates.html`) in the project root

## Current Project State
- Planning document exists: `plan.md`
- Agent behavior rules exist: `AGENTS.md`
- Prompt history exists: `prompts.md`
- Input data is available in `data/`:
  - `eurofxref.csv`
  - `eurofxref-hist.csv`
- Small module layout scaffold exists with `app/` package and placeholder files.

## Working Principles
- Keep implementation simple, typed, and readable for a second-year student.
- Prefer pragmatic solutions and explicit edge-case handling.
- Avoid over-engineering.

## Memory Bank Update Rule
After any project change (code, docs, structure, or rules), update this file to reflect:
1. What changed
2. Why it changed
3. Current status of the project

This file is the single AI-facing memory snapshot and must stay up to date.

## Latest Update (2026-02-28)
1. What changed
- Implemented daily CSV transform logic in `app/transform.py`:
  - Parses ECB date format.
  - Reads daily CSV safely.
  - Captures the latest available rates for `USD`, `SEK`, `GBP`, `JPY`.
  - Validates missing/invalid values with clear errors.
- Updated `main.py` to run this step and print latest date + selected currency rates.
- Logged the current user request in `prompts.md` as Prompt 11.

2. Why it changed
- This is the current incremental step from `plan.md`: parse daily rates and capture latest values for the selected currencies.

3. Current status
- Daily-rate parsing for target currencies is implemented and wired in the entry point.
- Historical parsing, mean calculation, and final markdown/html load step are still pending.

## Latest Update (2026-02-28, Historical Step)
1. What changed
- Added `parse_historical_rates_series` in `app/transform.py`.
  - Reads `data/eurofxref-hist.csv`.
  - Collects full time-series values as `(date, rate)` pairs for `USD`, `SEK`, `GBP`, `JPY`.
  - Skips blank and `N/A` values safely.
  - Validates invalid numeric values and ensures each target currency has data.
- Updated `main.py` to call the historical parser and print a compact summary (count + latest point).
- Logged the new user request in `prompts.md` as Prompt 12.

2. Why it changed
- This implements the next planned transform step: parse historical rates and collect full time-series for selected currencies.

3. Current status
- Daily rates parsing is complete.
- Historical time-series parsing for target currencies is complete.
- Mean historical-rate calculation and final table output generation are pending.

## Latest Update (2026-02-28, Mean + Formatting Step)
1. What changed
- Added `compute_mean_historical_rates` to calculate arithmetic mean per target currency.
- Added `format_rate` helper with a shared decimal precision rule (4 decimals) for consistent output rounding.
- Updated `main.py` to print a clean three-column preview:
  - `Currency Code`
  - `Rate`
  - `Mean Historical Rate`
- Logged the new user request in `prompts.md` as Prompt 13.

2. Why it changed
- This implements the next planned transform step: compute mean historical rates and apply consistent output formatting.

3. Current status
- Daily parsing is complete.
- Historical series parsing is complete.
- Historical mean calculation is complete.
- Consistent numeric formatting is complete.
- Final load to `exchange_rates.md` / `exchange_rates.html` is still pending.

## Latest Update (2026-02-28, Console Column Alignment)
1. What changed
- Updated `main.py` console output to use fixed-width aligned columns for:
  - `Currency Code`
  - `Rate`
  - `Mean Historical Rate`
- Added a separator line under the header for readability.
- Logged the new user request in `prompts.md` as Prompt 14.

2. Why it changed
- To make terminal output easier to read by keeping values visually attached to stable columns.

3. Current status
- Transform steps (daily parse, historical parse, mean calculation, formatting) are complete.
- Console preview output is now aligned and readable.
- Final file load step (`exchange_rates.md`/`exchange_rates.html`) remains pending.

## Latest Update (2026-02-28, Load Step Complete)
1. What changed
- Implemented markdown load logic in `app/load.py`:
  - `build_exchange_rates_markdown(...)` builds a 3-column markdown table.
  - `write_exchange_rates_markdown(...)` writes output to file.
- Updated `main.py` to:
  - Build ordered rows for `USD`, `SEK`, `GBP`, `JPY`.
  - Write final output to `exchange_rates.md` in the project root.
  - Keep aligned console preview output.
- Logged the new user request in `prompts.md` as Prompt 15.

2. Why it changed
- To complete plan step 4 (Load): persist transformed results into a final markdown table file.

3. Current status
- Transform pipeline is complete.
- Load pipeline is complete for markdown output.
- Running `python main.py` now generates `exchange_rates.md` successfully.
- Remaining work is final validation/polish and documentation cleanup for submission readiness.

## Latest Update (2026-02-28, Git Tracking Decision Guidance)
1. What changed
- Logged a user decision prompt in `prompts.md` (Prompt 16) about whether generated output should be committed or ignored.

2. Why it changed
- To keep prompt history complete and comply with project rules.

3. Current status
- Recommended approach: keep `exchange_rates.md` tracked in Git for this assignment deliverable.
