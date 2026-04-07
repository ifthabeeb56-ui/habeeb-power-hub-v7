import yfinance as download
import pandas as pd
import pandas_ta as ta

def get_stock_data(ticker, period="1y"):
    """സ്റ്റോക്ക് ഡാറ്റ ഡൗൺലോഡ് ചെയ്യാനുള്ള ഫംഗ്ഷൻ"""
    data = download.Ticker(ticker).history(period=period)
    return data

def add_indicators(df):
    """EMA, RSI തുടങ്ങിയ ഇൻഡിക്കേറ്ററുകൾ ചേർക്കുന്നു"""
    if df.empty:
        return df
    
    # EMA കണക്കുകൂട്ടലുകൾ
    df['EMA_20'] = ta.ema(df['Close'], length=20)
    df['EMA_50'] = ta.ema(df['Close'], length=50)
    df['EMA_200'] = ta.ema(df['Close'], length=200)
    
    # RSI കണക്കുകൂട്ടൽ
    df['RSI'] = ta.rsi(df['Close'], length=14)
    
    return df

def get_live_price(ticker):
    """ഏറ്റവും പുതിയ വില അറിയാൻ"""
    data = download.Ticker(ticker).history(period="1d")
    if not data.empty:
        return round(data['Close'].iloc[-1], 2)
    return 0.0
