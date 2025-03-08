import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Industrial Analytics - OEE"
)

#left_co, cent_co,last_co = st.columns(3)
#with cent_co:
#    st.image('./Mídia/analytics.jpg', width=600)


# -- Criar o sidebar
with st.sidebar:
    logo_teste = Image.open('./Mídia/ind.png')
    st.image(logo_teste, width=300)
    st.subheader('INDUSTRIAL ANALYTICS')

    
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Metas OEE", "Pilares OEE_1", "Pilares OEE_2", "Pilares OEE_3", "Pilares OEE_4", "Pilares OEE_5", "Pilares OEE_6", "Pilares OEE_7"])

with tab1:
    st.write('O objetivo desse ')
    # Dados de exemplo
    dados = {
    'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Meta_OEE': [85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85],
    'Real_OEE': [80, 87, 83, 90, 88, 84, 86, 89, 82, 91, 87, 88]
}


    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal de OEE e os valores reais mensais de OEE.')

    # Criar gráfico de barras interativo com Plotly
    fig = px.bar(df, x='Mes', y='Real_OEE', color=df['Real_OEE'] >= df['Meta_OEE'],
                color_discrete_map={True: 'green', False: 'red'},
                labels={'color': 'Meta atingida'},
                title='Acompanhamento de Metas Mensais de OEE',
                category_orders={'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']})
    
    # Adicionar linha da meta
    fig.add_scatter(x=df['Mes'], y=df['Meta_OEE'], mode='lines+markers', name='Meta OEE',
                    line=dict(color='blue', dash='dash'))

    # Atualizar layout do gráfico
    fig.update_layout(xaxis_title='Meses', yaxis_title='OEE (%)')

    # Exibir gráfico no Streamlit
    st.plotly_chart(fig)

with tab2:
    st.write('O objetivo desse painel é trazer possibilidades de análises dos principais KPIs.')

    st.write('Gráfico de Barras')
    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Criar gráfico combinado com Plotly
    fig = go.Figure()

    # Adicionar barras para Disponibilidade
    fig.add_trace(go.Bar(
        x=df['Mes'],
        y=df['Real_Disponibilidade'],
        name='Real Disponibilidade',
        marker_color='blue'
    ))
    fig.add_trace(go.Scatter(
        x=df['Mes'],
        y=df['Meta_Disponibilidade'],
        name='Meta Disponibilidade',
        mode='lines+markers',
        line=dict(color='blue', dash='dash')
    ))

    # Adicionar barras para Qualidade
    fig.add_trace(go.Bar(
        x=df['Mes'],
        y=df['Real_Qualidade'],
        name='Real Qualidade',
        marker_color='green'
    ))
    fig.add_trace(go.Scatter(
        x=df['Mes'],
        y=df['Meta_Qualidade'],
        name='Meta Qualidade',
        mode='lines+markers',
        line=dict(color='green', dash='dash')
    ))

    # Adicionar barras para Performance
    fig.add_trace(go.Bar(
        x=df['Mes'],
        y=df['Real_Performance'],
        name='Real Performance',
        marker_color='red'
    ))
    fig.add_trace(go.Scatter(
        x=df['Mes'],
        y=df['Meta_Performance'],
        name='Meta Performance',
        mode='lines+markers',
        line=dict(color='red', dash='dash')
    ))

    # Adicionar barras para OEE
    fig.add_trace(go.Bar(
        x=df['Mes'],
        y=df['Real_OEE'],
        name='Real OEE',
        marker_color='purple'
    ))
    fig.add_trace(go.Scatter(
        x=df['Mes'],
        y=df['Meta_OEE'],
        name='Meta OEE',
        mode='lines+markers',
        line=dict(color='purple', dash='dash')
    ))

    # Atualizar layout do gráfico
    fig.update_layout(
        barmode='group',
        xaxis_title='Meses',
        yaxis_title='Valores (%)',
        title='Acompanhamento de Metas Mensais de OEE e Componentes',
    )

    # Exibir gráfico no Streamlit

    st.plotly_chart(fig)

with tab3:
    st.write('O objetivo desse painel é trazer possibilidades de análises dos principais KPIs.')

    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Função para criar gráfico de radar com Plotly
    def criar_grafico_radar(df: pd.DataFrame, mes: str):
        categorias = ['Disponibilidade', 'Qualidade', 'Performance', 'OEE']
        
        meta_valores = [
            df[df['Mes'] == mes]['Meta_Disponibilidade'].values[0],
            df[df['Mes'] == mes]['Meta_Qualidade'].values[0],
            df[df['Mes'] == mes]['Meta_Performance'].values[0],
            df[df['Mes'] == mes]['Meta_OEE'].values[0]
        ]
        
        real_valores = [
            df[df['Mes'] == mes]['Real_Disponibilidade'].values[0],
            df[df['Mes'] == mes]['Real_Qualidade'].values[0],
            df[df['Mes'] == mes]['Real_Performance'].values[0],
            df[df['Mes'] == mes]['Real_OEE'].values[0]
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=meta_valores,
            theta=categorias,
            fill='toself',
            name='Meta'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=real_valores,
            theta=categorias,
            fill='toself',
            name='Real'
        ))
        
        fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, max(meta_valores + real_valores) + 10]
            )),
        showlegend=True,
        title=f'Gráfico de Radar - {mes}',
        width=1000,
        height=800
        )
        
        return fig

    # Selecionar mês para visualização
    mes_selecionado = st.selectbox('Selecione o mês:', df['Mes'].unique())

    # Criar gráfico de radar para o mês selecionado
    fig_radar = criar_grafico_radar(df=df, mes=mes_selecionado) # type: ignore

    # Exibir gráfico no Streamlit
    st.plotly_chart(fig_radar)

with tab4:
    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Função para criar gráfico de linha com áreas empilhadas com Plotly
    def criar_grafico_area_empilhada(df: pd.DataFrame):
        fig = px.area(df,
                    x='Mes',
                    y=['Real_Disponibilidade', 'Real_Qualidade', 'Real_Performance'],
                    title='Gráfico de Linha com Áreas Empilhadas - Componentes do OEE',
                    labels={'value': 'Valores (%)', 'variable': 'Componentes'},
                    color_discrete_map={
                        'Real_Disponibilidade': 'blue',
                        'Real_Qualidade': 'green',
                        'Real_Performance': 'red'
                    })
        
        fig.add_scatter(x=df['Mes'], y=df['Meta_OEE'], mode='lines+markers', name='Meta OEE',
                        line=dict(color='purple', dash='dash'))
        
        fig.add_scatter(x=df['Mes'], y=df['Real_OEE'], mode='lines+markers', name='Real OEE',
                        line=dict(color='purple'))
        
        fig.update_layout(xaxis_title='Meses', yaxis_title='Valores (%)')
        
        return fig

    # Criar gráfico de linha com áreas empilhadas
    fig_area_empilhada = criar_grafico_area_empilhada(df=df)

    # Exibir gráfico no Streamlit
    st.plotly_chart(fig_area_empilhada)

with tab5:

    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Função para criar gráfico de bolhas com Plotly
    def criar_grafico_bolhas(df: pd.DataFrame):
        fig = px.scatter(df,
                        x='Real_Disponibilidade',
                        y='Real_Performance',
                        size='Real_OEE',
                        color='Real_Qualidade',
                        hover_name='Mes',
                        title='Gráfico de Bolhas - Componentes do OEE',
                        labels={'Real_Disponibilidade': 'Disponibilidade (%)',
                                'Real_Performance': 'Performance (%)',
                                'Real_OEE': 'OEE (%)',
                                'Real_Qualidade': 'Qualidade (%)'})
        
        fig.update_layout(xaxis_title='Disponibilidade (%)', yaxis_title='Performance (%)')
        
        return fig

    # Criar gráfico de bolhas
    fig_bolhas = criar_grafico_bolhas(df=df)

    # Exibir gráfico no Streamlit
    st.plotly_chart(fig_bolhas)

with tab6:
    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Função para criar gráfico de barras empilhadas com Plotly
    def criar_grafico_barras_empilhadas(df: pd.DataFrame):
        fig = px.bar(df,
                    x='Mes',
                    y=['Real_Disponibilidade', 'Real_Qualidade', 'Real_Performance'],
                    title='Gráfico de Barras Empilhadas - Componentes do OEE',
                    labels={'value': 'Valores (%)', 'variable': 'Componentes'},
                    color_discrete_map={
                        'Real_Disponibilidade': 'blue',
                        'Real_Qualidade': 'green',
                        'Real_Performance': 'red'
                    })
        
        fig.add_scatter(x=df['Mes'], y=df['Meta_OEE'], mode='lines+markers', name='Meta OEE',
                        line=dict(color='purple', dash='dash'))
        
        fig.add_scatter(x=df['Mes'], y=df['Real_OEE'], mode='lines+markers', name='Real OEE',
                        line=dict(color='purple'))
        
        fig.update_layout(xaxis_title='Meses', yaxis_title='Valores (%)')
        
        return fig

    # Criar gráfico de barras empilhadas
    fig_barras_empilhadas = criar_grafico_barras_empilhadas(df=df)

    # Exibir gráfico no Streamlit
    fig_barras_empilhadas # type: ignore

with tab7:

    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Função para criar heatmap com Plotly
    def criar_heatmap(df: pd.DataFrame):
        df_melted = df.melt(id_vars=['Mes'], value_vars=['Meta_Disponibilidade', 'Real_Disponibilidade',
                                                        'Meta_Qualidade', 'Real_Qualidade',
                                                        'Meta_Performance', 'Real_Performance',
                                                        'Meta_OEE', 'Real_OEE'])
        
        fig = px.density_heatmap(df_melted,
                                x='Mes',
                                y='variable',
                                z='value',
                                color_continuous_scale='Viridis',
                                title='Heatmap - Componentes do OEE')
        
        fig.update_layout(xaxis_title='Meses', yaxis_title='Componentes')
        
        return fig

    # Criar heatmap
    fig_heatmap = criar_heatmap(df=df)

    # Exibir heatmap no Streamlit
    st.plotly_chart(fig_heatmap)

with tab8:

    # Dados de exemplo
    dados = {
        'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Meta_Disponibilidade': [95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95],
        'Real_Disponibilidade': [93, 96, 94, 97, 96, 94, 95, 97, 93, 98, 96, 97],
        'Meta_Qualidade': [98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98, 98],
        'Real_Qualidade': [97, 99, 97, 99, 98, 97, 98, 99, 96, 99, 98, 99],
        'Meta_Performance': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],
        'Real_Performance': [88, 91, 89, 92, 91, 89, 90, 92, 88, 93, 91, 92]
    }

    # Calcular OEE
    dados['Meta_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Meta_Disponibilidade'], dados['Meta_Qualidade'], dados['Meta_Performance'])]
    dados['Real_OEE'] = [d * q * p / (100**2) for d,q,p in zip(dados['Real_Disponibilidade'], dados['Real_Qualidade'], dados['Real_Performance'])]

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Configurar o layout do Streamlit
    st.title('Acompanhamento de Metas Mensais de OEE')
    st.write('Este gráfico mostra a meta mensal e os valores reais mensais de OEE e seus componentes: Disponibilidade, Qualidade e Performance.')

    # Função para criar gráfico de barras interativo com Plotly
    def criar_grafico(df: pd.DataFrame, coluna_meta: str, coluna_real: str, titulo: str): # type: ignore
        fig = px.bar(df,
                    x='Mes',
                    y=coluna_real,
                    color=df[coluna_real] >= df[coluna_meta],
                    color_discrete_map={True: 'green', False: 'red'},
                    labels={'color': 'Meta atingida'},
                    title=titulo,
                    category_orders={'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']})
        
        # Adicionar linha da meta
        fig.add_scatter(x=df['Mes'], y=df[coluna_meta], mode='lines+markers', name='Meta',
                        line=dict(color='blue', dash='dash'))
        
        # Atualizar layout do gráfico
        fig.update_layout(xaxis_title='Meses', yaxis_title=titulo)
        
        return fig

    # Criar gráficos para cada métrica
    fig_oee = criar_grafico(df=df,
                            coluna_meta='Meta_OEE',
                            coluna_real='Real_OEE',
                            titulo='OEE (%)')

    fig_disponibilidade = criar_grafico(df=df,
                                        coluna_meta='Meta_Disponibilidade',
                                        coluna_real='Real_Disponibilidade',
                                        titulo='Disponibilidade (%)')

    fig_qualidade = criar_grafico(df=df,
                                coluna_meta='Meta_Qualidade',
                                coluna_real='Real_Qualidade',
                                titulo='Qualidade (%)')

    fig_performance = criar_grafico(df=df,
                                    coluna_meta='Meta_Performance',
                                    coluna_real='Real_Performance',
                                    titulo='Performance (%)')

    # Exibir gráficos no Streamlit
    st.plotly_chart(fig_oee)
    st.plotly_chart(fig_disponibilidade)
    st.plotly_chart(fig_qualidade)
    st.plotly_chart(fig_performance)