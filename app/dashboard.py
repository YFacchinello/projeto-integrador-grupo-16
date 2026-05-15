import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

st.set_page_config(page_title="Projeto Integrador - Grupo 16", layout="wide")

@st.cache_data
def carregar_e_tratar_dados():
    caminho_dados = "data/personal_transactions.csv"
    
    if not os.path.exists(caminho_dados):
        st.error(f"Arquivo não encontrado no caminho: {caminho_dados}")
        st.stop()
        
    df = pd.read_csv(caminho_dados)
    
    mapeamento_colunas = {
        'Date': 'Data',
        'Category': 'Categoria',
        'Amount': 'Valor'
    }
    df = df.rename(columns=mapeamento_colunas)
    
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    df = df.dropna(subset=['Data', 'Valor'])
    
    df['Tipo'] = np.where(df['Transaction Type'] == 'credit', 'Entrada', 'Saída')
    df['Valor_Absoluto'] = df['Valor'].abs()
    df['Ano'] = df['Data'].dt.year
    
    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    df['Mes'] = df['Data'].dt.month.map(meses_pt)
    df['Ano_Mes'] = df['Data'].dt.to_period('M').astype(str)
    
    return df

df = carregar_e_tratar_dados()

st.sidebar.header("Filtros de Período")

anos_disponiveis = sorted(df['Ano'].unique())
ano_selecionado = st.sidebar.selectbox("Selecione o Ano", anos_disponiveis, index=len(anos_disponiveis)-1)

df_ano = df[df['Ano'] == ano_selecionado]

ordem_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
meses_no_ano = [m for m in ordem_meses if m in df_ano['Mes'].unique()]
mes_selecionado = st.sidebar.selectbox("Selecione o Mês", meses_no_ano)

df_filtrado = df_ano[df_ano['Mes'] == mes_selecionado]

st.title("📊 Dashboard de Gestão de Finanças Pessoais e Investimentos")
st.markdown("---")

receitas_mes = df_filtrado[df_filtrado['Tipo'] == 'Entrada']['Valor_Absoluto'].sum()
despesas_mes = df_filtrado[df_filtrado['Tipo'] == 'Saída']['Valor_Absoluto'].sum()
saldo_mes = receitas_mes - despesas_mes

if receitas_mes > 0:
    pct_economia = (saldo_mes / receitas_mes) * 100
else:
    pct_economia = 0.0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Saldo Total do Mês", value=f"R$ {saldo_mes:,.2f}")

with col2:
    st.metric(label="Total de Gastos no Mês", value=f"R$ {despesas_mes:,.2f}")

with col3:
    st.metric(label="Percentual de Economia", value=f"{pct_economia:.1f}%")

st.markdown("---")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("🍩 Distribuição de Gastos por Categoria")
    df_gastos = df_filtrado[df_filtrado['Tipo'] == 'Saída']
    if not df_gastos.empty:
        df_pizza = df_gastos.groupby('Categoria')['Valor_Absoluto'].sum().reset_index()
        fig_rosca = px.pie(
            df_pizza, 
            values='Valor_Absoluto', 
            names='Categoria', 
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_rosca, use_container_width=True)
    else:
        st.info("Nenhum gasto registrado neste período.")

with col_graf2:
    st.subheader("📊 Comparativo Mensal: Receita vs. Despesa")
    df_comp = df_filtrado.groupby('Tipo')['Valor_Absoluto'].sum().reset_index()
    if not df_comp.empty:
        fig_barras = px.bar(
            df_comp, 
            x='Tipo', 
            y='Valor_Absoluto', 
            color='Tipo',
            color_discrete_map={'Entrada': '#2ecc71', 'Saída': '#e74c3c'},
            text_auto='.2s'
        )
        st.plotly_chart(fig_barras, use_container_width=True)
    else:
        st.info("Sem dados para gerar o comparativo.")

st.markdown("---")

st.subheader("📋 Últimas Transações do Período")

colunas_desejadas = ['Data', 'Description', 'description', 'Categoria', 'Tipo', 'Valor_Absoluto']
colunas_existentes = [col for col in colunas_desejadas if col in df_filtrado.columns]

df_tabela = df_filtrado[colunas_existentes].sort_values(by='Data', ascending=False).copy()
df_tabela['Data'] = df_tabela['Data'].dt.strftime('%d/%m/%Y')
st.dataframe(df_tabela, use_container_width=True)