import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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
    st.subheader("Faturamento por Item (Cores Customizadas)")
    # 1. Definir cores específicas para cada item (em ordem alfabética)
cores_personalizadas = {
    "Coca-Cola": "#FF0000",  # Vermelho
    "Suco": "#FFA500",       # Laranja
    "X-Bacon": "#8B4513",    # Marrom
    "X-Salada": "00FF00"     # Verde
}

# 2. Extrair os itens e as cores na ordem correta
itens_ordenados = sorted(faturamento_por_item.index)
cores = [cores_personalizadas[item] for item in itens_ordenados]

# 3. Plotar o gráfico
fig, ax = plt.subplots()
fat_por_item.plot.pie(
    autopct="%.1f%%",
    colors=cores,
    startangle=90,        # Começa a pizza no topo
    wedgeprops={"edgecolor": "white", "linewidth": 1},  # Bordas brancas
    textprops={"fontsize": 10, "color": "black"},       # Cor do texto
    ax=ax
)
ax.set_ylabel("")  # Remove o label do eixo Y (que aparece por padrão)
st.pyplot(fig)

except FileNotFoundError:
    st.error("Erro: Arquivo 'lanchonete.csv' não encontrado. Verifique se:")
    st.write("- O arquivo está na **mesma pasta** que este script;")
    st.write("- O nome do arquivo está **exatamente igual** (incluindo .csv);")
    st.write("- Você salvou como 'Todos os arquivos', não como .txt.")
