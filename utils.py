import yfinance as yf
import pandas as pd

def get_live_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        return round(data['Close'].iloc[-1], 2) if not data.empty else 0.0
    except:
        return 0.0

# Nifty 500 ലിസ്റ്റ് കൊണ്ടുവരാൻ
def get_nifty500_tickers():
    try:
        url = "https://raw.githubusercontent.com/anirban-d/nifty-indices-constituents/main/ind_nifty500list.csv"
        n500_df = pd.read_csv(url)
        return sorted(n500_df['Symbol'].tolist())
    except:
        # ഇന്റർനെറ്റ് ഇല്ലെങ്കിൽ താഴെ കാണുന്ന ലിസ്റ്റ് സജഷൻ ആയി വരും
        return ["RELIANCE", "TCS", "HDFCBANK", "INFY", "SBIN"]
