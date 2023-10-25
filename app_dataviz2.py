import streamlit as st
import pandas as pd
from datetime import date 
import plotly.express as px 

st.title('Furtos de Veículos em SP')

st.sidebar.header('Filtros')

dados = pd.read_csv('../1_bases_tratadas/dados_GERAL.csv', encoding='utf-8', sep=',')
dados.columns = dados.columns.str.lower()

lista_opcoes = ['Univariado', 'Bivariado']
escolha_tipo_analise = st.sidebar.selectbox('Escolha o tipo de analise', lista_opcoes)

if escolha_tipo_analise=='Bivariado':
    auxiliar = dados.groupby(['descricaolocal'])['descricaolocal'].agg(['count'])
    auxiliar = auxiliar.reset_index().rename(columns={'count':'descricaolocalcount'})
    dados = pd.merge(dados, auxiliar, how='left', on='descricaolocal')

    fig = px.box(data_frame=dados, x='descr_tipo_veiculo', y='cidade')
    st.plotly_chart(fig)
    st.markdown('Podemos observar que não há relação entre o tipo de veículo roubado e a cidade')
    
    dados['freq'] = dados.groupby('peridoocorrencia')['peridoocorrencia'].transform('count') 
    fig2 = px.bar(data_frame=dados,x= 'peridoocorrencia',y='freq')
    st.plotly_chart(fig2)
    st.markdown('Pode-se observar que o período do dia que mais houve ocorrências registradas foi pela manhã com mais de dez mil registros, seguido pelo período da tarde com quase oito mil e cem registros.')

else:
    coluna_selecionada = st.sidebar.selectbox("Coluna", dados.columns)
    data_counts = dados[coluna_selecionada].value_counts()
    pie_data = pd.DataFrame({'names': data_counts.index, 'values': data_counts.values})
    fig = px.pie(pie_data, names='names', values='values', title=f'Gráfico de Pizza - {coluna_selecionada}')
    st.plotly_chart(fig)