import yfinance as yf
import pandas as pd

def get_live_price(ticker):
    try:
        # ticker symbol ശരിയാണെന്ന് ഉറപ്പുവരുത്തുക (eg: RELIANCE.NS)
        stock = yf.Ticker(ticker)
        # വളരെ കുറഞ്ഞ സമയത്തെ ഡാറ്റ എടുക്കുന്നു
        data = stock.history(period="1d", interval="1m")
        
        if not data.empty:
            return round(data['Close'].iloc[-1], 2)
        else:
            # ലൈവ് ഡാറ്റ കിട്ടിയില്ലെങ്കിൽ ഒടുവിലത്തെ ക്ലോസിംഗ് പ്രൈസ് നോക്കുന്നു
            data = stock.history(period="5d")
            return round(data['Close'].iloc[-1], 2) if not data.empty else 0.0
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return 0.0

def add_indicators(df):
    if df.empty:
        return df
    # EMA കണക്കുകൂട്ടുന്നു
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()
    df['EMA_200'] = df['Close'].ewm(span=200, adjust=False).mean()
    
    # RSI കണക്കുകൂട്ടുന്നു
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df
    
