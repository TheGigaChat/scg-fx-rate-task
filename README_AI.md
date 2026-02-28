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
