import streamlit as st
import plotly.express as px
import pandas as pd
from utils import get_live_price

def show_heatmap(portfolio_df):
    st.subheader("🔍 Portfolio Heatmap Analysis")
    
    if portfolio_df is None or portfolio_df.empty:
        st.warning("പോർട്ട്‌ഫോളിയോയിൽ സ്റ്റോക്കുകൾ ഒന്നുമില്ല. ആദ്യം സ്റ്റോക്കുകൾ ആഡ് ചെയ്യുക.")
        return

    # ഹീറ്റ്മാപ്പിന് ആവശ്യമായ ഡാറ്റ കണക്കാക്കുന്നു
    plot_data = []
    
    with st.spinner("Fetching latest prices for heatmap..."):
        for _, row in portfolio_df.iterrows():
            symbol = row['symbol']
            qty = row['qty']
            buy_price = row['buy_price']
            
            current_price = get_live_price(symbol)
            
            if current_price > 0:
                investment = buy_price * qty
                current_value = current_price * qty
                pnl = current_value - investment
                pnl_pct = (pnl / investment) * 100 if investment > 0 else 0
                
                plot_data.append({
                    "Symbol": symbol,
                    "Investment": round(investment, 2),
                    "Current Value": round(current_value, 2),
                    "PnL %": round(pnl_pct, 2),
                    "Live Price": current_price
                })

    if not plot_data:
        st.error("ഡാറ്റ ലഭ്യമാക്കാൻ കഴിഞ്ഞില്ല.")
        return

    df_plot = pd.DataFrame(plot_data)

    # Plotly Treemap നിർമ്മാണം
    fig = px.treemap(
        df_plot,
        path=['Symbol'],
        values='Investment',
        color='PnL %',
        color_continuous_scale='RdYlGn',  # നഷ്ടത്തിന് ചുവപ്പും ലാഭത്തിന് പച്ചയും
        color_continuous_midpoint=0,
        hover_data=['Live Price', 'Investment', 'PnL %'],
        height=500
    )

    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10))
    st.plotly_chart(fig, use_container_width=True)
            
