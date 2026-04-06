import pandas as pd
import os

PORTFOLIO_FILE = "portfolio_v7.csv"

def load_data():
    try:
        if os.path.exists(PORTFOLIO_FILE):
            return pd.read_csv(PORTFOLIO_FILE)
        else:
            # ഫയൽ ഇല്ലെങ്കിൽ പുതിയൊരു ബ്ലാങ്ക് ടേബിൾ റിട്ടേൺ ചെയ്യുന്നു
            return pd.DataFrame(columns=["Category", "Name", "Buy Price", "QTY", "Investment", "Status"])
    except:
        return pd.DataFrame(columns=["Category", "Name", "Buy Price", "QTY", "Investment", "Status"])
