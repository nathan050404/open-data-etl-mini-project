import pandas as pd
import yfinance as yf
from pathlib import Path

def extract_data(ticker, period="1mo"):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period=period)
    return data

def transform_data(df):
    print("Transforming data...")
    df = df.reset_index() 
    df = df.round(2) 
    return df

def load_data(df, output_path):
    print(f"Saving data to {output_path}...")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True) 
    df.to_csv(output_path, index=False) 
    print("Workflow complete!")

if __name__ == "__main__":
    TICKER = "AAPL"
    SAVE_PATH = "data/processed/output.csv"

    raw_data = extract_data(TICKER)
    clean_data = transform_data(raw_data)
    load_data(clean_data, SAVE_PATH)