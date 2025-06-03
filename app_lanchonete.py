import pandas as pd
import streamlit as st

# Configuração inicial
st.title("🍔 Análise de Vendas - Lanchonete")

# 1. Ler o CSV
try:
    df = pd.read_csv("lanchonete.csv")  # Lê o arquivo
    st.success("CSV carregado com sucesso! Veja as primeiras linhas:")
    st.write(df.head())  # Mostra os dados

    # 2. Gráfico de barras (vendas por item)
    st.subheader("Itens Mais Vendidos")
    vendas_por_item = df.groupby("Item")["Quantidade"].sum()
    st.bar_chart(vendas_por_item)

    # 3. Gráfico de pizza (faturamento por item)
    st.subheader("Faturamento por Item")
    df["Faturamento"] = df["Quantidade"] * df["Preco"]  # Calcula o faturamento
    faturamento_por_item = df.groupby("Item")["Faturamento"].sum()
    st.pyplot(faturamento_por_item.plot.pie(autopct="%.1f%%").figure)

except FileNotFoundError:
    st.error("Erro: Arquivo 'lanchonete.csv' não encontrado. Verifique se:")
    st.write("- O arquivo está na **mesma pasta** que este script;")
    st.write("- O nome do arquivo está **exatamente igual** (incluindo .csv);")
    st.write("- Você salvou como 'Todos os arquivos', não como .txt.")
