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
    t_inv, t_val = 0, 0

    for _, row in df.iterrows():
        ltp = get_live_price(row['symbol'])
        inv = row['buy_price'] * row['qty']
        val = ltp * row['qty']
        pnl = (val + row['dividend']) - (inv + row['tax'])
        
        t_inv += inv
        t_val += val
        
        portfolio_data.append({
            "Account": row['account'],
            "Stock": row['symbol'],
            "Qty": row['qty'],
            "Buy Price": f"₹{row['buy_price']:.2f}",
            "LTP": f"₹{ltp:.2f}",
            "Current Value": f"₹{val:.2f}",
            "P&L": pnl,
            "P%": (pnl/inv*100) if inv > 0 else 0
        })

    # Summary Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Investment", f"₹{t_inv:,.2f}")
    c2.metric("Current Value", f"₹{t_val:,.2f}", f"{(t_val-t_inv):,.2f}")
    c3.metric("Total Gain %", f"{((t_val-t_inv)/t_inv*100 if t_inv>0 else 0):.2f}%")

    st.markdown("---")
    
    # Account Filter
    acc_filter = st.radio("അക്കൗണ്ട് മാറ്റുക:", ["All", "Habeeb", "RISU"], horizontal=True)
    p_df = pd.DataFrame(portfolio_data)
    if acc_filter != "All":
        p_df = p_df[p_df['Account'] == acc_filter]

    st.dataframe(p_df, use_container_width=True, hide_index=True)

def add_stock_form():
    if st.toggle("➕ Add/Remove/Update Stock"):
        with st.form("stock_form"):
            col1, col2 = st.columns(2)
            symbol = col1.text_input("Symbol (eg: TCS.NS)")
            b_date = col2.date_input("Purchase Date", datetime.now())
            cat = col1.selectbox("Category", ["Equity", "ETF", "Mutual Fund"])
            acc = col2.selectbox("Account", ["Habeeb", "RISU"])
            price = col1.number_input("Buy Price", min_value=0.0)
            qty = col2.number_input("Quantity", min_value=1)
            tax = col1.number_input("Tax", min_value=0.0)
            
            if st.form_submit_button("Save to Portfolio"):
                if symbol:
                    add_stock_db(symbol.upper(), price, qty, cat, acc, tax, str(b_date))
                    st.success("സേവ് ചെയ്തു!")
                    st.rerun()
