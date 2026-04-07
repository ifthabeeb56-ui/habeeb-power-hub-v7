import yfinance as yf
import pandas as pd
import pandas_ta as ta

def get_stock_data(ticker, period="1y"):
    data = yf.Ticker(ticker).history(period=period)
    return data

def get_live_price(ticker):
    """സ്റ്റോക്കിന്റെ ലൈവ് വില എടുക്കുന്നു"""
    try:
        data = yf.Ticker(ticker).history(period="1d")
        if not data.empty:
            return round(data['Close'].iloc[-1], 2)
        return 0.0
    except:
        return 0.0

def get_nifty500_tickers():
    """Nifty 500 ലിസ്റ്റ് NSE-യിൽ നിന്ന് എടുക്കുന്നു"""
    url = "https://archives.nseindia.com/content/indices/ind_nifty500list.csv"
    try:
        df = pd.read_csv(url)
        tickers = (df['Symbol'] + ".NS").tolist()
        return tickers
    except:
        return ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
