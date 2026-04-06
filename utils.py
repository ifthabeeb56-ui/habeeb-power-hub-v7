import pandas as pd
import os

PORTFOLIO_FILE = "portfolio_v7.csv"

def load_data():
    if os.path.exists(PORTFOLIO_FILE):
        return pd.read_csv(PORTFOLIO_FILE)
    # ഫയൽ ഇല്ലെങ്കിൽ വെറും ഒരു ലിസ്റ്റ് മാത്രം നൽകുന്നു
    return pd.DataFrame(columns=["Category", "Name", "Buy Price", "QTY", "Investment", "Status"])
