import streamlit as st
import pandas as pd
from database import get_portfolio_db, add_stock_db
from utils import get_live_price
from datetime import datetime

def show_portfolio():
    df = get_portfolio_db()
    if df.empty:
        st.info("പോർട്ട്‌ഫോളിയോയിൽ സ്റ്റോക്കുകൾ ഒന്നുമില്ല.")
        return

    portfolio_data = []
    for _, row in df.iterrows():
        ltp = get_live_price(row['symbol'])
        inv = row['buy_price'] * row['qty']
        val = ltp * row['qty']
        # നെറ്റ് പ്രോഫിറ്റ് = (നിലവിലെ വില + ഡിവിഡന്റ്) - (വാങ്ങിയ വില + ടാക്സ്)
        pnl = (val + row['dividend']) - (inv + row['tax'])
        
        portfolio_data.append({
            "Account": row['account'],
            "Stock": row['symbol'],
            "Qty": row['qty'],
            "Buy Price": row['buy_price'],
            "LTP": ltp,
            "Investment": inv,
            "Current Value": val,
            "P&L": pnl,
            "P%": (pnl/inv*100) if inv > 0 else 0
        })

    p_df = pd.DataFrame(portfolio_data)
    
    # അക്കൗണ്ട് തിരിച്ചുള്ള സംഗ്രഹം (Summary)
    acc = st.selectbox("Select Account View", ["All", "Habeeb", "RISU"])
    if acc != "All":
        p_df = p_df[p_df['Account'] == acc]

    st.dataframe(p_df.style.format(precision=2), use_container_width=True)

def add_stock_form():
    if st.toggle("➕ Add Stock"):
        with st.form("add_form"):
            col1, col2 = st.columns(2)
            symbol = col1.text_input("Symbol (eg: RELIANCE.NS)")
            b_date = col2.date_input("Purchase Date", datetime.now())
            
            cat = col1.selectbox("Category", ["Equity", "ETF", "Mutual Fund"])
            acc = col2.selectbox("Account", ["Habeeb", "RISU"])
            
            price = col1.number_input("Buy Price", min_value=0.0)
            qty = col2.number_input("Qty", min_value=1)
            tax = col1.number_input("Tax", min_value=0.0)
            
            if st.form_submit_button("Save Stock"):
                add_stock_db(symbol.upper(), price, qty, cat, acc, tax, str(b_date))
                st.success("Saved!")
                st.rerun()
        
