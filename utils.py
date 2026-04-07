import yfinance as yf
import pandas as pd

def get_live_price(ticker):
    try:
        # ടിക്കർ ശരിയാണോ എന്ന് പരിശോധിക്കുന്നു
        full_ticker = ticker if ".NS" in ticker or ".BO" in ticker else f"{ticker}.NS"
        stock = yf.Ticker(full_ticker)
        # ഏറ്റവും പുതിയ വില എടുക്കുന്നു
        data = stock.fast_info
        return round(data['last_price'], 2)
    except:
        return 0.0

def get_nifty500_tickers():
    try:
        url = "https://raw.githubusercontent.com/anirban-d/nifty-indices-constituents/main/ind_nifty500list.csv"
        n500_df = pd.read_csv(url)
        return sorted(n500_df['Symbol'].tolist())
    except:
        return ["RELIANCE", "TCS", "HDFCBANK", "INFY", "SBIN"]
