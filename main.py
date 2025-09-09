import streamlit as st
from utils import carregar_dados_acao, criar_grafico_cotacao, ACOES_BANCARIAS

# Configuração da página
st.set_page_config(
    page_title="Analisador de Cotações Bancárias",
    page_icon="📈",
    layout="wide"
)

def main():
    # Título da aplicação
    st.title("📈 Analisador de Cotações Bancárias")
    st.markdown("Analise o histórico de cotações de ações bancárias brasileiras.")
    
    # Sidebar para seleções
    st.sidebar.header("Configurações")
    
    # Seleção da ação
    acao_selecionada = st.sidebar.selectbox(
        "Escolha a ação bancária:", list(ACOES_BANCARIAS.keys())
    )
    
    # Seleção do período
    periodo = st.sidebar.slider("Período (anos):", 1, 10, 5)
    
    # Obter código da ação
    codigo_acao = ACOES_BANCARIAS[acao_selecionada]
    
    # Carregar dados
    with st.spinner(f"Carregando dados de {acao_selecionada}..."):
        dados = carregar_dados_acao(codigo_acao, periodo)
    
    if not dados.empty:
        # Exibir métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Preço Atual", f"R$ {dados['Close'].iloc[-1]:.2f}",
                     f"{((dados['Close'].iloc[-1] / dados['Close'].iloc[-2] - 1) * 100):.2f}%")
        with col2:
            st.metric("Maior Preço", f"R$ {dados['High'].max():.2f}")
        with col3:
            st.metric("Menor Preço", f"R$ {dados['Low'].min():.2f}")
        with col4:
            st.metric("Volume Médio", f"{dados['Volume'].mean():,.0f}")
        
        # Criar e exibir gráfico
        fig = criar_grafico_cotacao(dados, f"Histórico - {acao_selecionada}")
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        
        # Exibir tabela de dados
        st.subheader("📊 Dados Detalhados")
        mostrar_todos = st.checkbox("Mostrar todos os dados")
        dados_exibir = dados if mostrar_todos else dados.tail(30)
        st.dataframe(dados_exibir.round(2), use_container_width=True)
        
        # Botão para download
        csv = dados.to_csv()
        st.download_button("📥 Baixar dados em CSV", csv, 
                          f"{codigo_acao}_{periodo}anos.csv", "text/csv")
    else:
        st.error("Não foi possível carregar os dados. Tente novamente.")

# Executar aplicação
if __name__ == "__main__":
    main()