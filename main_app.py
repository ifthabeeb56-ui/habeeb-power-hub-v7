import streamlit as st
from utils import load_data
import plotly.express as px

st.set_page_config(page_title="Habeeb Stock Hub", layout="wide")
st.title("📈 എന്റെ സ്റ്റോക്ക് പോർട്ട്‌ഫോളിയോ")

df = load_data()
st.write("പുതിയ ഡാറ്റ ആഡ് ചെയ്യാൻ Portfolio പേജ് ഉപയോഗിക്കുക.")

if not df.empty:
    st.dataframe(df)
else:
    st.info("നിലവിൽ ഡാറ്റ ഒന്നുമില്ല. പുതിയതായി തുടങ്ങാം!")
