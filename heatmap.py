import streamlit as st
import plotly.express as px
from utils import get_live_price

def show_heatmap(portfolio_df):
    st.subheader("📊 Portfolio Heatmap")
    
    if portfolio_df.empty:
        st.warning("പോർട്ട്‌ഫോളിയോയിൽ സ്റ്റോക്കുകൾ ഒന്നുമില്ല. ആദ്യം സ്റ്റോക്കുകൾ ആഡ് ചെയ്യുക.")
        return

    # ഹീറ്റ്മാപ്പിന് ആവശ്യമായ ഡാറ്റ തയ്യാറാക്കുന്നു
    # ഇവിടെ നമ്മൾ ഓരോ സ്റ്റോക്കിന്റെയും നിലവിലെ വിലയും ലാഭശതമാനവും കണക്കാക്കുന്നു
    plot_data = []
    for index, row in portfolio_df.iterrows():
        current_price = get_live_price(row['symbol'])
        investment = row['buy_price'] * row['qty']
        current_value = current_price * row['qty']
        pnl_pct = ((current_value - investment) / investment) * 100 if investment > 0 else 0
        
        plot_data.append({
            "Symbol": row['symbol'],
            "Investment": investment,
            "PnL %": pnl_pct,
            "Current Price": current_price
        })

    import pandas as pd
    df_plot = pd.DataFrame(plot_data)

    # Treemap (Heatmap) നിർമ്മിക്കുന്നു
    fig = px.treemap(
        df_plot,
        path=['Symbol'],
        values='Investment',
        color='PnL %',
        color_continuous_scale='RdYlGn', # ചുവപ്പ് (നഷ്ടം), പച്ച (ലാഭം)
        hover_data=['Current Price', 'PnL %']
    )

    st.plotly_chart(fig, use_container_width=True)
