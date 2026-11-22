# Project name

> One sentence: what this agent watches, and what it does when something looks wrong.

**Live app:** link-to-your-streamlit-app &nbsp;·&nbsp; **30-second overview:** link-to-your-video

## The problem

Two or three sentences from your questionnaire: who does this today, how, and why it hurts.

## How it works

```
generator (1 import/min) → inbox/ → Detect (file name, SHA-256) → Land raw in TinyDB
→ MoE router → Jev classifies → Claude extracts values → Validate → Load clean rows into Turso (SQL)
→ Decide (statistical test) → Publish  OR  Hold + alert → a person releases
→ Streamlit dashboard → daily summary → Claude Routine writes the daily report
```

All data in this project is simulated. No real people, customers or employees appear in it.

## Run it on your laptop

1. Copy `.env.example` to `.env` and fill it in (see [SETUP.md](SETUP.md)).
2. `uv sync`
3. `uv run python scripts/check_setup.py`
4. `uv run streamlit run streamlit_app.py`

## Portfolio BINGO

★ = required. Change `[ ]` to `[x]` and replace `link` with a link to the proof (a file, chart, screenshot, workflow run or the live app).
**Minimum to finish:** all 16 ★ squares, plus at least 2 squares in the N (Numbers) column, which makes 18 of 24.

| B: Build & ETL | I: Intelligence (MoE) | N: Numbers | G: Go live | O: Operations |
| --- | --- | --- | --- | --- |
| [ ] ★ [Agent loop runs every minute](link) | [ ] ★ [Jev classifies records](link) | [ ] [Descriptive stats with 95% CIs](link) | [ ] ★ [Forecast graph with prediction interval](link) | [ ] ★ [Pipeline and tests on GitHub Actions](link) |
| [ ] ★ [File names logged](link) | [ ] ★ [Claude extracts to a JSON schema](link) | [ ] [Hypothesis test](link) | [ ] ★ [Stat trigger takes a visible action](link) | [ ] ★ [App live on Streamlit Community Cloud](link) |
| [ ] ★ [Raw data landed in TinyDB](link) | [ ] ★ [MoE router with model-usage view](link) | [x] FREE: [Case-study data generator](link) | [ ] ★ [Live flow chart](link) | [ ] ★ [Claude Routine daily report](link) |
| [ ] ★ [Clean data in SQLite](link) | [ ] [Jev vs. Claude on the gold set](link) | [ ] [Correlation or regression](link) | [ ] ★ [SQL and formulas shown per step](link) | [ ] ★ [30-second Claude Motion overview](link) |
| [ ] [Snowflake warehouse (optional)](link) | [ ] [Prompt injection caught and logged](link) | [ ] [Anomaly detection](link) | [ ] [Backtest beats the naive baseline](link) | [ ] ★ [Governance docs and human review](link) |

## AI assistance

This project was built with Claude Code (Claude Team) and uses Jev and Claude at runtime through an application-level mixture-of-experts router.

- **What Claude Code wrote:** ...
- **What I changed and why:** ...
- **Where an AI was wrong, and how I caught it:** ...
- **Which expert handled what, and what my tests showed (Jev vs. Claude):** ...
- **What I would do differently:** ...
