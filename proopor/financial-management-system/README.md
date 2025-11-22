# Sistema de Gestão Financeira

Este projeto é um sistema completo para gestão financeira, desenvolvido para ajudar usuários a gerenciar seus dados financeiros de forma eficiente. Inclui funcionalidades para entrada de dados, processamento financeiro, análise, visualização e geração de relatórios, tudo acessível por uma interface amigável em Streamlit.

## Estrutura do Projeto

```
financial-management-system
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── input.py
│   │   └── sample_data.csv
│   ├── processing
│   │   ├── __init__.py
│   │   └── financial_processing.py
│   ├── analysis
│   │   ├── __init__.py
│   │   └── metrics.py
│   ├── visualization
│   │   ├── __init__.py
│   │   └── plots.py
│   ├── reporting
│   │   ├── __init__.py
│   │   └── report.py
│   └── interface
│       ├── __init__.py
│       └── streamlit_app.py
├── requirements.txt
└── README.md
```

## Funcionalidades

- **Entrada de Dados**: Carregue e limpe dados financeiros a partir de arquivos CSV e Excel.
- **Processamento Financeiro**: Processe os dados para construir fluxo de caixa e gerar relatórios.
- **Análise**: Calcule métricas financeiras importantes e analise o impacto das despesas.
- **Visualização**: Crie visualizações diversas para representar os dados financeiros de forma clara.
- **Relatórios**: Gere relatórios em Excel e PDF com resumo dos dados e insights financeiros.
- **Interface do Usuário**: Aplicativo Streamlit para facilitar a interação e gestão dos dados.

## Instruções de Instalação

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd financial-management-system
   ```

2. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   pip install streamlit
   ```

3. Execute o aplicativo Streamlit:
   ```
   streamlit run src/interface/streamlit_app.py
   ```

## Guia de Uso

- Faça upload dos seus arquivos de dados financeiros pela interface do Streamlit.
- Selecione o período de análise e as métricas que deseja visualizar.
- Gere e baixe relatórios conforme sua necessidade.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugestões de melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.