import streamlit as st
import pandas as pd
from database import get_portfolio_db, add_stock_db
from utils import get_live_price

def show_portfolio():
    df = get_portfolio_db()
    
    if df.empty:
        st.info("പോർട്ട്‌ഫോളിയോയിൽ സ്റ്റോക്കുകൾ ഒന്നുമില്ല.")
        return

    # --- Summary Section ---
    portfolio_data = []
    total_inv = 0
    total_val = 0

    for _, row in df.iterrows():
        live_price = get_live_price(row['symbol'])
        inv = row['buy_price'] * row['qty']
        curr_val = live_price * row['qty']
        
        total_inv += inv
        total_val += curr_val

        portfolio_data.append({
            "Stock": row['symbol'],
            "Qty": row['qty'],
            "Buy Price": f"₹{row['buy_price']:.2f}",
            "LTP": f"₹{live_price:.2f}",
            "Current Value": f"₹{curr_val:.2f}",
            "P&L": f"₹{(curr_val - inv):.2f}"
        })

    # കാർഡുകൾ കാണിക്കുന്നു
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Investment", f"₹{total_inv:,.2f}")
    c2.metric("Current Value", f"₹{total_val:,.2f}", f"{(total_val-total_inv):,.2f}")
    c3.metric("Total Gain %", f"{((total_val-total_inv)/total_inv*100 if total_inv>0 else 0):.2f}%")

    st.markdown("---")
    
    # സ്റ്റോക്ക് ലിസ്റ്റ് കാണിക്കുന്നു
    st.dataframe(pd.DataFrame(portfolio_data), use_container_width=True)

def add_stock_form():
    # സ്വിച്ച് (Toggle) ഉപയോഗിച്ച് ഫോം കാണിക്കണോ എന്ന് തീരുമാനിക്കാം
    show_form = st.toggle("➕ Add New Stock Form")
    
    if show_form:
        with st.expander("Enter Stock Details", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                symbol = st.text_input("Symbol (eg: RELIANCE.NS)")
            with col2:
                price = st.number_input("Buy Price", min_value=0.0)
            with col3:
                qty = st.number_input("Quantity", min_value=1)
            
            if st.button("Save to Portfolio"):
                if symbol:
                    add_stock_db(symbol.upper(), price, qty)
                    st.success(f"{symbol} ആഡ് ചെയ്തു!")
                    st.rerun()
    
