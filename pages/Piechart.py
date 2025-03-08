import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Industrial Analytics - Piechart"
)

st.header(":bar_chart: ANALYTICS INDUSTRIAL")

# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Mídia/ind.png')
    st.image(logo_teste, width=300)
    st.subheader('MENU - ANALYTICS')
    


# Exemplo de dados
data = {
    'Causa': ['Parada programada', 'Parada Não programada', 'Eventos externos', 'Parada operacional', 'Outros'],
    'Paradas': [15, 25, 10, 20, 5]
}

df = pd.DataFrame(data)
st.table(df)

# Configurando o Streamlit
st.title('Distribuição de Causas de Paradas de Equipamentos')

# Criando o gráfico de pie chart
fig = px.pie(df, values='Paradas', names='Causa', title='Distribuição de Causas de Paradas de Equipamentos')

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)