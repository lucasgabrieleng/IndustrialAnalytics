import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Industrial Analytics - HeatMap"
)

# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Mídia/ind.png')
    st.image(logo_teste, width=300)
    st.subheader('INDUSTRIAL ANALYTICS')
    

st.header(":bar_chart: ANALYTICS INDUSTRIAL")


# Exemplo de dados
data = {
    'Equipamento': ['A', 'B', 'C', 'D', 'E'],
    'OEE': [85, 88, 90, 92, 87],
    'Disponibilidade': [95, 96, 94, 97, 95],
    'Qualidade': [90, 91, 89, 93, 92]
}

df = pd.DataFrame(data)

# Seleção de variáveis para o Heatmap
st.subheader('Selecione até 3 variáveis para o Heatmap')
variaveis_selecionadas = st.multiselect(
    'Variáveis',
    ['OEE', 'Disponibilidade', 'Qualidade'],
    default=['OEE', 'Disponibilidade', 'Qualidade']
)

if len(variaveis_selecionadas) > 3:
    st.write("Por favor selecione no máximo três variáveis para o Heatmap.")
else:
    # Configurando o Streamlit
    st.title('Heatmap de KPIs por Equipamento')

    # Criando o heatmap
    fig, ax = plt.subplots(figsize=(10, 6))
    heatmap = sns.heatmap(df.set_index('Equipamento')[variaveis_selecionadas], annot=True, cmap='coolwarm', linewidths=.5, ax=ax)

    # Título do gráfico
    ax.set_title('Heatmap de KPIs por Equipamento')

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)