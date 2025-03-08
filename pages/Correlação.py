import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
#from fpdf import FPDF

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Industrial Analytics - Correlação"
)

st.header(":bar_chart: ANALYTICS INDUSTRIAL")


# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Mídia/ind.png')
    st.image(logo_teste, width=300)
    st.subheader('INDUSTRIAL ANALYTICS')
    
# Exemplo de dados com datas
data = {
    'Data': pd.date_range(start='2023-01-01', periods=8, freq='M'),
    'OEE': [85, 88, 90, 92, 87, 85, 91, 89],
    'Disponibilidade': [95, 96, 94, 97, 95, 93, 96, 94],
    'Performance': [92, 95, 93, 98, 97, 96, 94, 90],
    'Qualidade': [99, 98, 100, 95, 93, 97, 98, 99]
}

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])  # Certifique-se de que a coluna de datas está no formato datetime

# Habilitar Correlação OEE e Disponibilidade
display_oee_disp = st.checkbox('Mostrar Correlação OEE e Disponibilidade')
if display_oee_disp:
    st.title('Correlação entre OEE e Disponibilidade')
    st.write('Use o slider para selecionar o intervalo de datas.')

    # Slider para selecionar o intervalo de datas
    start_date_disp, end_date_disp = st.slider(
        'Selecione o intervalo de datas para OEE e Disponibilidade',
        min_value=df['Data'].min().to_pydatetime(),
        max_value=df['Data'].max().to_pydatetime(),
        value=(df['Data'].min().to_pydatetime(), df['Data'].max().to_pydatetime()),
        format="MM/DD/YYYY",
        key='slider_oee_disp'
    )

    # Convertendo os valores do slider para datetime
    start_date_disp = pd.to_datetime(start_date_disp)
    end_date_disp = pd.to_datetime(end_date_disp)

    # Filtrando os dados com base no intervalo de datas selecionado
    filtered_df_disp = df[(df['Data'] >= start_date_disp) & (df['Data'] <= end_date_disp)]

    # Criando o gráfico de dispersão
    fig_disp = px.scatter(filtered_df_disp, x='Disponibilidade', y='OEE', title='Correlação entre OEE e Disponibilidade')
    st.plotly_chart(fig_disp)

# Habilitar Correlação OEE e Performance
display_oee_perf = st.checkbox('Mostrar Correlação OEE e Performance')
if display_oee_perf:
    st.title('Correlação entre OEE e Performance')
    st.write('Use o slider para selecionar o intervalo de datas.')

    # Slider para selecionar o intervalo de datas
    start_date_perf, end_date_perf = st.slider(
        'Selecione o intervalo de datas para OEE e Performance',
        min_value=df['Data'].min().to_pydatetime(),
        max_value=df['Data'].max().to_pydatetime(),
        value=(df['Data'].min().to_pydatetime(), df['Data'].max().to_pydatetime()),
        format="MM/DD/YYYY",
        key='slider_oee_perf'
    )

    # Convertendo os valores do slider para datetime
    start_date_perf = pd.to_datetime(start_date_perf)
    end_date_perf = pd.to_datetime(end_date_perf)

    # Filtrando os dados com base no intervalo de datas selecionado
    filtered_df_perf = df[(df['Data'] >= start_date_perf) & (df['Data'] <= end_date_perf)]

    # Criando o gráfico de dispersão
    fig_perf = px.scatter(filtered_df_perf, x='Performance', y='OEE', title='Correlação entre OEE e Performance')
    st.plotly_chart(fig_perf)

# Multiseleção de Indicadores para Correlação
st.subheader('Selecione os Indicadores para Correlação')
indicadores_selecionados = st.multiselect(
    'Indicadores',
    ['OEE', 'Disponibilidade', 'Performance', 'Qualidade'],
    default=['OEE', 'Disponibilidade']
)

if len(indicadores_selecionados) == 2:
    indicador_x = indicadores_selecionados[0]
    indicador_y = indicadores_selecionados[1]

    st.title(f'Correlação entre {indicador_x} e {indicador_y}')
    
    # Slider para selecionar o intervalo de datas
    start_date_multi, end_date_multi = st.slider(
        f'Selecione o intervalo de datas para {indicador_x} e {indicador_y}',
        min_value=df['Data'].min().to_pydatetime(),
        max_value=df['Data'].max().to_pydatetime(),
        value=(df['Data'].min().to_pydatetime(), df['Data'].max().to_pydatetime()),
        format="MM/DD/YYYY",
        key='slider_multi'
    )

    # Convertendo os valores do slider para datetime
    start_date_multi = pd.to_datetime(start_date_multi)
    end_date_multi = pd.to_datetime(end_date_multi)

    # Filtrando os dados com base no intervalo de datas selecionado
    filtered_df_multi = df[(df['Data'] >= start_date_multi) & (df['Data'] <= end_date_multi)]

    # Criando o gráfico de dispersão
    fig_multi = px.scatter(filtered_df_multi, x=indicador_x, y=indicador_y,
                           title=f'Correlação entre {indicador_x} e {indicador_y}')
    
    st.plotly_chart(fig_multi)
elif len(indicadores_selecionados) > 2:
    st.write("Por favor selecione no máximo dois indicadores para correlacionar.")
else:
    st.write("Por favor selecione exatamente dois indicadores para correlacionar.")

# Matriz de Correlação
st.title('Matriz de Correlação dos KPIs Selecionados')

# Seleção de variáveis para a Matriz de Correlação
st.subheader('Selecione até 3 variáveis para a Matriz de Correlação')
variaveis_selecionadas_corr = st.multiselect(
    'Variáveis',
    ['OEE', 'Disponibilidade', 'Performance', 'Qualidade'],
)

if len(variaveis_selecionadas_corr) > 3:
    st.write("Por favor selecione no máximo três variáveis para a Matriz de Correlação.")
elif len(variaveis_selecionadas_corr) > 0:
    corr_df = df[variaveis_selecionadas_corr].corr()

    # Criando a matriz de correlação
    fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', linewidths=.5, ax=ax_corr)

    # Título do gráfico
    ax_corr.set_title('Matriz de Correlação dos KPIs Selecionados')

    # Exibindo a matriz de correlação no Streamlit
    st.pyplot(fig_corr)
else:
    st.write("Por favor selecione pelo menos um indicador para gerar a matriz de correlação.")
