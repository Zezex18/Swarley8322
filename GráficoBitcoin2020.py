import pandas as pd
import streamlit as st

try:
  tot_registros = df.count()['total']
except:
  df = pd.read_csv('BTC-2020min.csv.zip')

st.bar_chart(df, x='data', y='preço_fechamento')
