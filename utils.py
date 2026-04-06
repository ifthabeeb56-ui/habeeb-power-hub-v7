import pandas as pd
import yfinance as yf
import os

PORTFOLIO_FILE = "portfolio_v7.csv"

def load_data():
    if os.path.exists(PORTFOLIO_FILE):
        return pd.read_csv(PORTFOLIO_FILE)
    return pd.DataFrame(columns=["Category", "Name", "Buy Price", "QTY", "Investment", "Status"])

def update_prices(df):
    # ലൈവ് പ്രൈസ് അപ്‌ഡേറ്റ് ചെയ്യാനുള്ള ഫങ്ക്ഷൻ
    return df
