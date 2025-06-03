import pandas as pd
import streamlit as st
import plotly.express as px

url = "https://raw.githubusercontent.com/plotly/datasets/master/bitcoin.csv"
df = pd.read_csv(url)

# Converter data
df['Date'] = pd.to_datetime(df['Date'])

# Dashboard
st.title("💰 Análise de Bitcoin (Dataset Simplificado)")

# Gráfico 1: Preço de fechamento
st.subheader("Preço Histórico (USD)")
fig = px.line(df, x='Date', y='Close', 
              labels={'Close': 'Preço (USD)', 'Date': 'Data'},
              color_discrete_sequence=['#00BFFF'])  # Cor azul
st.plotly_chart(fig, use_container_width=True)
