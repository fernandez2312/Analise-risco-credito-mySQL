# Análise de Risco de Crédito: Minimizando Inadimplência com Python e MySQL

## 1. Contexto de Negócio
O controle de inadimplência é um dos maiores desafios de instituições financeiras e fintechs de crédito. Uma concessão de crédito ineficiente gera um aumento direto na Provisão para Devedores Duvidosos (PDD), impactando a rentabilidade líquida da operação. O objetivo deste projeto é analisar uma base histórica real de 32.500+ registros de empréstimos para identificar variáveis críticas de risco e propor políticas de crédito orientadas a dados.

## 2. Estrutura do Projeto e Tecnologias
* **Ingestão de Dados:** Carga rápida em blocos de arquivos CSV para banco de dados relacional via **Python (Pandas e SQLAlchemy)**.
* **Banco de Dados:** Armazenamento, modelagem e queries de agregação analítica utilizando **MySQL**.
* **Métricas Avaliadas:** Taxa de inadimplência por segmento ($T_i$), faixas etárias, perfis de moradia e intenção do empréstimo.

## 3. Principais Descobertas (Insights de Negócio)
* **Tratamento de Ruídos:** Identificação e limpeza de inconsistências reais no dataset (dados demográficos distorcidos e taxas de juros ausentes).
* **Fatores de Risco:** Segmentação analítica mapeando quais perfis de tomadores concentram o maior volume financeiro inadimplente.

## 4. Próximos Passos
* [ ] Implementação de visualizações executivas (Dashboard) conectadas ao banco MySQL.
* [ ] Desenvolvimento de um modelo preditivo básico em Python para score de crédito.
