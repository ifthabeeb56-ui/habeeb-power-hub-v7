import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect("portfolio.db")
    c = conn.cursor()
    # പഴയ കോഡിലെ എല്ലാ കോളങ്ങളും ഇവിടെ ആഡ് ചെയ്യുന്നു
    c.execute('''CREATE TABLE IF NOT EXISTS stocks 
                 (symbol TEXT, buy_price REAL, qty INTEGER, 
                  category TEXT, account TEXT, tax REAL, dividend REAL, buy_date TEXT)''')
    conn.commit()
    conn.close()

def add_stock_db(symbol, price, qty, category, account, tax, buy_date):
    conn = sqlite3.connect("portfolio.db")
    c = conn.cursor()
    c.execute("INSERT INTO stocks (symbol, buy_price, qty, category, account, tax, dividend, buy_date) VALUES (?,?,?,?,?,?,?,?)",
              (symbol, price, qty, category, account, tax, 0.0, buy_date))
    conn.commit()
    conn.close()

def get_portfolio_db():
    conn = sqlite3.connect("portfolio.db")
    try:
        df = pd.read_sql("SELECT * FROM stocks", conn)
    except:
        df = pd.DataFrame()
    conn.close()
    return df
    import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect("portfolio.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stocks 
                 (symbol TEXT, buy_price REAL, qty INTEGER)''')
    conn.commit()
    conn.close()

def add_stock_db(symbol, price, qty):
    conn = sqlite3.connect("portfolio.db")
    df = pd.DataFrame([[symbol, price, qty]], columns=['symbol', 'buy_price', 'qty'])
    df.to_sql("stocks", conn, if_exists="append", index=False)
    conn.close()

def get_portfolio_db():
    conn = sqlite3.connect("portfolio.db")
    try:
        df = pd.read_sql("SELECT * FROM stocks", conn)
    except:
        df = pd.DataFrame(columns=['symbol', 'buy_price', 'qty'])
    conn.close()
    return df
