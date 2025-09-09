import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import streamlit as st

# Dicionário com ações bancárias brasileiras
ACOES_BANCARIAS = {
    "Itaú Unibanco": "ITUB4.SA",
    "Banco do Brasil": "BBAS3.SA",
    "Bradesco": "BBDC4.SA",
    "Santander Brasil": "SANB11.SA",
    "BTG Pactual": "BPAC11.SA",
    "Banco Inter": "BIDI11.SA",
    "Nubank": "NU",
    "XP Inc": "XP"
}

@st.cache_data
def carregar_dados_acao(codigo_acao, periodo_anos=5):
    """
    Carrega dados históricos de uma ação usando yfinance.
    
    Args:
        codigo_acao (str): Código da ação (ex: 'ITUB4.SA')
        periodo_anos (int): Período em anos para buscar dados
    
    Returns:
        pandas.DataFrame: DataFrame com dados históricos da ação
    """
    try:
        # Calcular data de início
        data_fim = datetime.now()
        data_inicio = data_fim - timedelta(days=periodo_anos * 365)
        
        # Baixar dados
        ticker = yf.Ticker(codigo_acao)
        dados = ticker.history(
            start=data_inicio.strftime('%Y-%m-%d'),
            end=data_fim.strftime('%Y-%m-%d')
        )
        
        return dados
    
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

def criar_grafico_cotacao(dados, titulo):
    """
    Cria um gráfico de candlestick com os dados da ação.
    
    Args:
        dados (pandas.DataFrame): DataFrame com dados da ação
        titulo (str): Título do gráfico
    
    Returns:
        plotly.graph_objects.Figure: Gráfico plotly
    """
    try:
        fig = go.Figure(data=go.Candlestick(
            x=dados.index,
            open=dados['Open'],
            high=dados['High'],
            low=dados['Low'],
            close=dados['Close'],
            name="Cotação"
        ))
        
        fig.update_layout(
            title=titulo,
            yaxis_title="Preço (R$)",
            xaxis_title="Data",
            template="plotly_white",
            height=500
        )
        
        return fig
    
    except Exception as e:
        st.error(f"Erro ao criar gráfico: {e}")
        return None