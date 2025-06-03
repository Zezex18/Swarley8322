import pandas as pd
import streamlit as st

# Carregar o arquivo CSV
df = pd.read_csv("BTC-2020min.csv")

# Converter a coluna de data para datetime
df['date'] = pd.to_datetime(df['date'])

# Criar uma nova coluna com o mês/ano
df['month'] = df['date'].dt.to_period('M')

# Calcular a média de fechamento por mês
monthly_avg = df.groupby('month')['close'].mean().reset_index()

# Converter 'month' de volta para datetime para o gráfico
monthly_avg['month'] = monthly_avg['month'].dt.to_timestamp()

# Exibir o gráfico
st.title("Média Mensal do Preço de Fechamento do BTC em 2020")
st.line_chart(monthly_avg, x='month', y='close')
