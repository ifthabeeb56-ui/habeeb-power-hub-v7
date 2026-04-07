import streamlit as st
from portfolio import show_portfolio, add_stock_form
from heatmap import show_heatmap
from database import get_portfolio_db
import pandas as pd

st.set_page_config(page_title="Habeeb's Power Hub v7", layout="wide")

st.title("📊 Habeeb's Power Hub v7")

# പുതിയ ടാബ് സെക്ഷൻ
tabs = st.tabs(["🔍 Heatmap", "💼 Portfolio", "⚙️ Data Management", "📈 Analytics"])

df = get_portfolio_db()

with tabs[0]:
    show_heatmap(df)

with tabs[1]:
    add_stock_form()
    show_portfolio()

with tabs[2]:
    st.subheader("📥 Export / 📤 Import Data")
    
    # Download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Portfolio CSV", csv, "portfolio_backup.csv", "text/csv")
    
    st.markdown("---")
    
    # Upload
    uploaded_file = st.file_uploader("Upload Portfolio CSV", type=["csv"])
    if uploaded_file is not None:
        new_data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:")
        st.dataframe(new_data)
        if st.button("Confirm Import"):
            # ഇവിടെ ഡാറ്റാബേസിലേക്ക് സേവ് ചെയ്യാനുള്ള കോഡ് വരും
            st.success("ഡാറ്റ വിജയകരമായി ഇംപോർട്ട് ചെയ്തു!")
    
