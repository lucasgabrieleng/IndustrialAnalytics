import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title='Analytics Industrial',
    page_icon="📊",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
            'About': "Aplicação de Analytics Industrial."
    }
)

#left_co, cent_co,last_co = st.columns(3)
#with cent_co:
#    st.image('./Mídia/analytics.jpg', width=600)


# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Mídia/ind.png')
    st.image(logo_teste, width=300)
    st.subheader('INDUSTRIAL ANALYTICS')

    

st.header(":bar_chart: ANALYTICS INDUSTRIAL")

tab1, tab2, tab3 = st.tabs(["Geral", "Sobre", "Simulador de KPIs"])

with tab1:
    st.write('O objetivo desse painel é fornecer análises de KPIs para a área industrial.')
    st.write('Dentre os KPIs mais utilizados estão: OEE, Disponibilidade, Performance e Qualidade.')
    st.write('OEE é a sigla em inglês para Overall Equipment Effectiveness, que significa Eficiência Global do Equipamento. É um indicador que mede a eficiência dos equipamentos industriais. '
             'O OEE é uma métrica fundamental na automação industrial. Ele é usado para calcular a contribuição dos equipamentos para o processo produtivo. '
             'O OEE é calculado com base em três pilares: '
             'Disponibilidade: Tempo disponível que a máquina tem para produzir, descontando as paradas '
             'Performance: Eficiência real do equipamento vs capacidade nominal '
             'Qualidade: Tempo de produção de produtos bons vs tempo total de produção')
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image('./Mídia/OEE.jpg', width=300, caption="Overall Equipment Effectiveness")
    
    
with tab2:
    st.write('Painel criado para teste de análise de KPIs Industriais.')
    st.write('Desenvolvido por: Lucas Gabriel')

with tab3:
    st.write('O objetivo desse painel é trazer possibilidades de análises dos principais KPIs.')
    st.write('(Em Desenvolvimento)')
    def create_plotly_speedometer(val, title, target):
        fig = go.Figure()

    # Create the gauge chart
        fig.add_trace(go.Indicator(
            mode="gauge+number+delta",
            value=val,
            title={'text': title},
            delta={'reference': target, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, target], 'color': "lightgray"},
                    {'range': [target, 100], 'color': "lightgray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': target}}))
        
        return fig
    with st.container():
        # Valores reais e metas dos indicadores
        val = st.slider('Valor Real (%)', 0, 100, 75)
        target = st.slider('Meta (%)', 0, 100, 85)

        # Cria o gráfico de velocímetro moderno com Plotly
        fig = create_plotly_speedometer(val, 'Indicador', target)

        # Exibe o gráfico no Streamlit
        st.plotly_chart(fig)
 

    




