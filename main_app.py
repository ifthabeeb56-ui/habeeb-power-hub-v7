import streamlit as st
from portfolio import show_portfolio, add_stock_form
from heatmap import show_heatmap        # ഇത് പുതുതായി ചേർത്തത്
from database import get_portfolio_db   # ഡാറ്റാബേസിൽ നിന്ന് സ്റ്റോക്കുകൾ എടുക്കാൻ

st.set_page_config(page_title="Habeeb's Power Hub v7", layout="wide")

st.title("📊 Habeeb's Power Hub v7")

# ടാബുകൾ സെറ്റ് ചെയ്യുന്നു
tabs = st.tabs(["🔍 Heatmap", "💼 Portfolio", "📈 Analytics", "📰 News"])

# പോർട്ട്‌ഫോളിയോ ഡാറ്റാബേസിൽ നിന്ന് എടുക്കുന്നു
df = get_portfolio_db()

with tabs[0]:
    # ഹീറ്റ്മാപ്പ് ഇവിടെ കാണിക്കുന്നു
    show_heatmap(df)

with tabs[1]:
    add_stock_form()
    show_portfolio()

with tabs[2]:
    st.info("Analytics ഫീച്ചർ ഉടനെ വരുന്നു...")

with tabs[3]:
    st.info("News ഫീച്ചർ ഉടനെ വരുന്നു...")
    
