import pandas as pd
import streamlit as st
import csv

try:
  tot_registros = df.count()['total']
except:
  df = pd.read_csv('BTC-2020.csv')

st.bar_chart(df, x='', y='t')
