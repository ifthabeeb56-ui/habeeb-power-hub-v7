import streamlit as st
from utils import load_data
import pandas as pd

st.set_page_config(layout="wide", page_title="Habeeb's Power Hub v7")

st.title("📊 Habeeb's Power Hub v7")

# ഡാറ്റ ലോഡ് ചെയ്യുന്നു
df = load_data()

# ഡാറ്റ ഉണ്ടോ എന്ന് പരിശോധിക്കുന്നു
if df.empty:
    st.info("നിലവിൽ പോർട്ട്‌ഫോളിയോയിൽ സ്റ്റോക്കുകൾ ഒന്നുമില്ല.")
    st.write("പുതിയ സ്റ്റോക്കുകൾ ആഡ് ചെയ്യാൻ ഇടത് വശത്തെ മെനുവിൽ നിന്നും **Portfolio** പേജ് ഉപയോഗിക്കുക.")
    
    # തൽക്കാലം ഒരു സാമ്പിൾ ടേബിൾ കാണിക്കാൻ (Optional)
    st.subheader("Sample View")
    sample_data = pd.DataFrame(columns=["Category", "Name", "Buy Price", "QTY", "Investment", "Status"])
    st.table(sample_data)
else:
    st.success("നിങ്ങളുടെ പോർട്ട്‌ഫോളിയോ ഡാറ്റ താഴെ കാണാം")
    st.dataframe(df)

st.sidebar.success("മുകളിലെ പേജുകൾ തിരഞ്ഞെടുക്കുക")
