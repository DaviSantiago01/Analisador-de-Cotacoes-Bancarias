# 📈 Analisador de Cotações Bancárias

Uma aplicação web desenvolvida em Streamlit para análise de cotações de ações bancárias brasileiras em tempo real.

## 🚀 Funcionalidades

- **Análise de Cotações**: Visualize o histórico de preços de ações bancárias brasileiras
- **Gráficos Interativos**: Gráficos de candlestick com Plotly para análise técnica
- **Métricas em Tempo Real**: Preço atual, maior/menor preço e volume médio
- **Período Personalizável**: Selecione o período de análise de 1 a 10 anos
- **Download de Dados**: Exporte os dados em formato CSV
- **Interface Intuitiva**: Design limpo e responsivo

## 🏦 Ações Disponíveis

- Itaú Unibanco (ITUB4.SA)
- Banco do Brasil (BBAS3.SA)
- Bradesco (BBDC4.SA)
- Santander Brasil (SANB11.SA)
- BTG Pactual (BPAC11.SA)
- Banco Inter (BIDI11.SA)
- Nubank (NU)
- XP Inc (XP)

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para aplicações web em Python
- **yfinance**: API para dados financeiros do Yahoo Finance
- **Plotly**: Biblioteca para gráficos interativos
- **Pandas**: Manipulação e análise de dados
- **NumPy**: Computação numérica

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/DaviSantiago01/Analisador-de-Cotacoes-Bancarias.git
cd Analisador-de-Cotacoes-Bancarias
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

1. Execute a aplicação:
```bash
streamlit run main.py
```

2. Abra seu navegador e acesse:
```
http://localhost:8501
```

## 📊 Como Usar

1. **Selecione uma Ação**: Use o menu lateral para escolher a ação bancária desejada
2. **Defina o Período**: Ajuste o slider para selecionar o período de análise (1-10 anos)
3. **Visualize os Dados**: Analise as métricas e o gráfico interativo
4. **Explore os Detalhes**: Visualize a tabela com dados históricos detalhados
5. **Baixe os Dados**: Use o botão de download para exportar os dados em CSV

## 📁 Estrutura do Projeto

```
Analisador-de-Cotacoes-Bancarias/
├── main.py              # Arquivo principal da aplicação
├── utils.py             # Funções auxiliares e configurações
├── requirements.txt     # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Documentação do projeto
```

## 🔍 Detalhes Técnicos

### Arquivos Principais

- **main.py**: Interface principal do Streamlit (máximo 100 linhas)
- **utils.py**: Contém as funções de carregamento de dados e criação de gráficos

### Funcionalidades do Código

- **Cache de Dados**: Utiliza `@st.cache_data` para otimizar o carregamento
- **Tratamento de Erros**: Implementa try/catch para robustez
- **Design Responsivo**: Layout adaptável para diferentes tamanhos de tela
- **Código Limpo**: Separação de responsabilidades entre arquivos

## 📈 Dados

Os dados são obtidos em tempo real através da API do Yahoo Finance via biblioteca `yfinance`. Incluem:

- Preços de abertura, fechamento, máxima e mínima
- Volume de negociação
- Dados históricos ajustados
- Informações de dividendos (quando aplicável)

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

- **Desenvolvedor**: Davi Santiago
- **GitHub**: [@DaviSantiago01](https://github.com/DaviSantiago01)
- **Projeto**: [Analisador de Cotações Bancárias](https://github.com/DaviSantiago01/Analisador-de-Cotacoes-Bancarias)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!