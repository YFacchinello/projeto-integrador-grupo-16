# projeto-integrador-grupo-16
Repositório para criação do projeto integrador de desenvolvimento low code em ciência de dados do curso de ADS - Senac

## Integrantes
- Aline Oliveira da Costa e Silva
- Kelly Domingos Fernandes
- Silpharny Marques Miranda
- Yuri de Abreu Facchinello

## Definição da base de dados

Base de Dados: Personal Finance Dataset (Kaggle). Link: https://www.kaggle.com/datasets/entrepreneurlife/personal-finance

- Contexto: Os dados consistem em registros de transações financeiras (receitas e despesas), categorizados por tipo (alimentação, lazer, moradia, salário, etc.) com datas e valores específicos.

- Objetivo da Análise: Transformar dados brutos de extratos em informações visuais que permitam ao usuário identificar para onde seu dinheiro está indo, qual sua taxa de economia mensal e quais categorias possuem maior impacto no orçamento.

## Objetivo

O objetivo central é fornecer ao usuário uma ferramenta de Low Code que transforme dados brutos de transações (extratos) em inteligência financeira. A análise visa:

- Identificar os maiores gargalos de consumo por categoria.

- Monitorar o rendimento de ativos em comparação com meses anteriores.

- Facilitar a tomada de decisão sobre economia e novos investimentos através de indicadores visuais claros.

## Planejamento

Tarefas por Integrante:

- Kelly e Aline: Pesquisa, seleção da base de dados e documentação técnica.

- Yuri e Silpharny: Estruturação do repositório, configuração do ambiente Streamlit e prototipagem visual.

Cronograma:

- Semana 1: Setup do GitHub e documentação inicial (Etapa atual).

- Semana 2: Exploração dos dados e limpeza inicial.

- Semana 3: Desenvolvimento das visualizações no Streamlit.

- Semana 4: Deploy e refinamento da interface.

Transformações Pretendidas:

- Conversão de formatos de data para filtros temporais.

- Agrupamento de valores por categoria e por tipo (Entrada vs. Saída).

- Cálculo de saldo acumulado mensal.

Visualizações e Métricas:

- Métricas (KPIs): Saldo Total, Total de Gastos no Mês, Percentual de Economia.

- Gráficos: Gráfico de Rosca (Distribuição de gastos por categoria), Gráfico de Barras (Comparativo mensal de Receita vs. Despesa) e Tabela Dinâmica com as últimas transações.

## Ideia inicial

O dashboard será dividido em uma barra lateral (Sidebar) para filtros de período e uma área central organizada em colunas. No topo, três indicadores rápidos exibirão a saúde financeira. Abaixo, dois gráficos principais darão a visão macro das finanças, finalizando com uma tabela detalhada para consulta rápida.

Dashboard de Gestão de Finanças Pessoais e Investimentos
