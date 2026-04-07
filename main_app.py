import streamlit as st
from portfolio import show_portfolio, add_stock_form

st.set_page_config(page_title="Power Hub v7", layout="wide")

st.title("Habeeb's Power Hub v7")

# ടാബുകൾ സെറ്റ് ചെയ്യുന്നു
tab1, tab2, tab3 = st.tabs(["📊 Portfolio", "🔥 Heat Map", "👀 Watchlist"])

with tab1:
    # സ്റ്റോക്ക് ആഡ് ചെയ്യാനുള്ള ഫോം
    add_stock_form()
    st.divider()
    # പോർട്ട്‌ഫോളിയോ ലിസ്റ്റ് കാണിക്കാൻ
    show_portfolio()

with tab2:
    st.header("Market Heat Map")
    st.info("ഈ ഫീച്ചർ ഉടൻ ലഭ്യമാകും.")

with tab3:
    st.header("Watchlist")
    st.info("വാച്ച് ലിസ്റ്റ് സെറ്റ് ചെയ്യാനുള്ള കോഡ് അടുത്ത സ്റ്റെപ്പിൽ ചെയ്യാം.")
    
