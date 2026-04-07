import streamlit as st

st.set_page_config(page_title="Power Hub v7", layout="wide")

st.title("Habeeb's Power Hub v7")

# ടാബുകൾ നിർമ്മിക്കുന്നു
tab1, tab2, tab3 = st.tabs(["📊 Portfolio", "🔥 Heat Map", "👀 Watchlist"])

with tab1:
    st.header("Your Portfolio")
    st.write("ഇവിടെ നിങ്ങളുടെ സ്റ്റോക്ക് വിവരങ്ങൾ വരും.")

with tab2:
    st.header("Market Heat Map")
    st.write("സെക്ടർ തിരിച്ചുള്ള സ്റ്റോക്ക് പെർഫോമൻസ് ഇവിടെ കാണാം.")

with tab3:
    st.header("Custom Watchlist")
    st.write("നിങ്ങൾ നിരീക്ഷിക്കുന്ന സ്റ്റോക്കുകളുടെ ലൈവ് ഡാറ്റ ഇവിടെ ക്രമീകരിക്കാം.")
