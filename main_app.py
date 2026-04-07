import streamlit as st
from portfolio import show_portfolio, add_stock_form
# ഇനി വരാനിരിക്കുന്ന ഫയലുകൾ
# from heatmap import show_heatmap
# from analytics import show_analytics

st.set_page_config(page_title="Habeeb's Power Hub v7", layout="wide")

st.title("📊 Habeeb's Power Hub v7")

# ടാബുകൾ സെറ്റ് ചെയ്യുന്നു
tabs = st.tabs(["🔍 Heatmap", "💼 Portfolio", "📈 Analytics", "📰 News"])

with tabs[0]:
    st.info("Heatmap ഫീച്ചർ ഉടനെ ആഡ് ചെയ്യുന്നതാണ്...")

with tabs[1]:
    add_stock_form()
    show_portfolio()

with tabs[2]:
    st.info("Analytics (EMA/RSI) ഫീച്ചർ ഉടനെ ആഡ് ചെയ്യുന്നതാണ്...")

with tabs[3]:
    st.info("News ഫീച്ചർ ഉടനെ ആഡ് ചെയ്യുന്നതാണ്...")
