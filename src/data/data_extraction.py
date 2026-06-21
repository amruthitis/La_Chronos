import yfinance as yf
import pandas as pd 
from pathlib import Path

if not Path("market_data.csv").exists():
    tickers = ["^GSPC","^VIX", "^TNX", "^IRX"]
    df = yf.download(tickers, start="2010-01-01", end="2026-01-01", interval="1d", auto_adjust=True)
    df.to_csv("market_data.csv")



