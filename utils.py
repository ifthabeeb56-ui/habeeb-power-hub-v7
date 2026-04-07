import pandas as pd

def get_nifty500_tickers():
    """Nifty 500 ലിസ്റ്റ് ഡൗൺലോഡ് ചെയ്യുന്നു"""
    url = "https://archives.nseindia.com/content/indices/ind_nifty500list.csv"
    try:
        df = pd.read_csv(url)
        # NSE സിംബലുകൾക്ക് ഒപ്പം '.NS' ചേർക്കുന്നു (yfinance-ന് വേണ്ടി)
        tickers = (df['Symbol'] + ".NS").tolist()
        return tickers
    except:
        # ഇന്റർനെറ്റ് ഇല്ലെങ്കിൽ ഉപയോഗിക്കാൻ ഒരു ബാക്കപ്പ് ലിസ്റ്റ്
        return ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
