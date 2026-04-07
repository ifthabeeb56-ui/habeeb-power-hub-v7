import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period="1y"):
    data = yf.Ticker(ticker).history(period=period)
    return data

def add_indicators(df):
    """pandas_ta ഇല്ലാതെ EMA-യും RSI-യും കണക്കാക്കുന്നു"""
    if df.empty:
        return df
    
    # EMA കണക്കുകൂട്ടുന്നു (Exponential Moving Average)
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()
    df['EMA_200'] = df['Close'].ewm(span=200, adjust=False).mean()
    
    # RSI കണക്കുകൂട്ടുന്നു (Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df

def get_live_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1d")
        return round(data['Close'].iloc[-1], 2) if not data.empty else 0.0
    except:
        return 0.0

def get_nifty500_tickers():
    url = "https://archives.nseindia.com/content/indices/ind_nifty500list.csv"
    try:
        df = pd.read_csv(url)
        return (df['Symbol'] + ".NS").tolist()
    except:
        return ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
