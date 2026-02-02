# Open Data ETL Mini-Project - Stock Data
**Source**: Yahoo Finance via the `yfinance` library.

## Project Steps
1. **Extract**: Downloaded 1 month of stock price data for Apple (AAPL).
2. **Transform**: Reset the index to make Date a column and rounded all values to 2 decimal places.
3. **Load**: Saved the cleaned data to `data/processed/output.csv`.

## How to Run
1. Install requirements: `pip install pandas yfinance`
2. Run script: `python src/main.py`