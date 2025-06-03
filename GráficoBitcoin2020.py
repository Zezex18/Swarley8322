import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

dates = pd.date_range(start="2023-01-01", periods=100)
prices = np.random.normal(loc=30000, scale=5000, size=100).cumsum()  # Simula tendência
volumes = np.random.randint(1000, 50000, size=100)

df = pd.DataFrame({
    "Date": dates,
    "Close": prices,
    "Volume": volumes,
    "Change %": np.random.uniform(-5, 5, 100)
})

st.title("📊 Bitcoin Fake Data (Para Teste Rápido)")

st.subheader("Preço Simulado (USD)")
fig = px.line(df, x="Date", y="Close", 
              labels={"Close": "Preço (USD)"},
              color_discrete_sequence=["#00BFFF"])
st.plotly_chart(fig)
