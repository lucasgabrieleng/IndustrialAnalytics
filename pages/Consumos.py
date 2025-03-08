import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Industrial Analytics - Consumos"
)

# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Mídia/ind.png')
    st.image(logo_teste, width=300)
    st.subheader('INDUSTRIAL ANALYTICS')

st.header(":bar_chart: ANALYTICS INDUSTRIAL")

# Exemplo de dados
data = {
    'Data': pd.date_range(start='2023-01-01', periods=12, freq='M').tolist() * 9,
    'Planta': ['Planta A'] * 36 + ['Planta B'] * 36 + ['Planta C'] * 36,
    'Insumo': (['Insumo 1'] * 12 + ['Insumo 2'] * 12 + ['Insumo 3'] * 12) * 3,
    'Consumo': [100, 110, 105, 115, 120, 125, 130, 135, 140, 145, 150, 155] +
               [90, 95, 85, 100, 105, 110, 115, 120, 125, 130, 135, 140] +
               [80, 85, 75, 90, 95, 100, 105, 110, 115, 120, 125, 130] +
               [70, 75, 65, 80, 85, 90, 95, 100, 105, 110, 115, 120] +
               [60, 65, 55, 70, 75, 80, 85, 90, 95, 100, 105, 110] +
               [50, 55, 45, 60, 65, 70, 75, 80, 85, 90, 95, 100] +
               [40, 45, 35, 50, 55, 60, 65, 70, 75, 80, 85, 90] +
               [30, 35, 25, 40, 45, 50, 55, 60, 65, 70, 75, 80] +
               [20, 25, 15, 30, 35, 40, 45, 50, 55, 60, 65, 70] 
              
}

df = pd.DataFrame(data)

# Configurando o Streamlit
st.title('Tendências de Consumo Específico de Insumos')

# Seleção de Local
local_selecionado = st.selectbox('Selecione a Planta', df['Planta'].unique())

# Filtrando os insumos disponíveis para o local selecionado
insumos_disponiveis = df[df['Planta'] == local_selecionado]['Insumo'].unique()

# Seleção de Insumo
insumo_selecionado = st.selectbox('Selecione o Insumo', insumos_disponiveis)

# Seleção do Período de Tempo com Slider
data_min = df['Data'].min()
data_max = df['Data'].max()
data_inicio, data_fim = st.slider(
    'Selecione o intervalo de datas',
    min_value=data_min.to_pydatetime(),
    max_value=data_max.to_pydatetime(),
    value=(data_min.to_pydatetime(), data_max.to_pydatetime()),
    format="MM/DD/YYYY"
)

# Convertendo os valores do slider para datetime
data_inicio = pd.to_datetime(data_inicio)
data_fim = pd.to_datetime(data_fim)

# Filtrando os dados com base nas seleções
df_filtrado = df[(df['Planta'] == local_selecionado) & 
                 (df['Insumo'] == insumo_selecionado) & 
                 (df['Data'] >= data_inicio) & 
                 (df['Data'] <= data_fim)]

# Criando o gráfico de linhas
fig = px.line(df_filtrado, x='Data', y='Consumo', title=f'Tendências de Consumo de {insumo_selecionado} em {local_selecionado}')

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)