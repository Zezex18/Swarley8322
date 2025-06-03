import pandas as pd
import streamlit as st
import csv

try:
  tot_registros = df.count()['total']
except:
  df = pd.read_csv('BTC-2020.csv')

st.line_chart(df, x='Data', y='Preço Fechamento')
