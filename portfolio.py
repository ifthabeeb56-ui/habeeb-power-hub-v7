import streamlit as st
from utils import get_live_price, get_nifty500_tickers

def add_stock_form():
    """സ്റ്റോക്ക് ആഡ് ചെയ്യാനുള്ള ഫോം"""
    with st.expander("➕ Add/Remove/Update Stock"):
        all_stocks = get_nifty500_tickers()
        selected_stock = st.selectbox("Select Symbol from Nifty 500", all_stocks)
        buy_price = st.number_input("Buy Price", min_value=0.0)
        qty = st.number_input("Qty", min_value=1)
        if st.button("Add to Portfolio"):
            st.success(f"{selected_stock} ആഡ് ചെയ്തിട്ടുണ്ട്!")

def show_portfolio():
    """പോർട്ട്‌ഫോളിയോ കാണിക്കാനുള്ള ഫംഗ്ഷൻ"""
    st.subheader("My Portfolio Holdings")
    my_stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
    
    for stock in my_stocks:
        price = get_live_price(stock)
        st.write(f"{stock}: ₹{price}")
