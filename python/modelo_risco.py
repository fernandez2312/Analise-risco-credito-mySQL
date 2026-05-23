import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Conexão com o banco MySQL
url_conexao = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="#Titi2312@", 
    host="localhost",
    port=3306,
    database="banco_risco"
)
engine = create_engine(url_conexao)

# 2. Carregar dados selecionando as variáveis preditoras (Features)
query = """
SELECT 
    person_age AS idade,
    person_income AS renda_anual,
    loan_amnt AS valor_emprestimo,
    loan_int_rate AS taxa_juros,
    loan_percent_income AS comprometimento_renda,
    loan_status AS inadimplente
FROM credit_risk_dataset
WHERE person_age <= 80;
"""
df = pd.read_sql(query, engine)

# Tratamento rápido de nulos específico para o modelo não quebrar
df['taxa_juros'] = df['taxa_juros'].fillna(df['taxa_juros'].median())

# 3. Divisão em Variáveis Preditoras (X) e Alvo (y)
X = df[['idade', 'renda_anual', 'valor_emprestimo', 'taxa_juros', 'comprometimento_renda']]
y = df['inadimplente']

# Separar 80% dos dados para treino e 20% para testar a inteligência do modelo
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Treinando o modelo de Machine Learning (Gradient Boosting)...")

# 4. Treinamento do Modelo Preditivo
modelo = GradientBoostingClassifier(random_state=42)
modelo.fit(X_treino, y_treino)

# 5. Avaliação do Modelo com os dados de teste
previsoes = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)

print("\n📊 --- PERFORMANCE DO MODELO PREDITIVO ---")
print(f"Acurácia Geral: {acuracia * 100:.2f}%")
print("\nRelatório de Classificação Detalhado:")
print(classification_report(y_teste, previsoes))

# 6. Importância das Variáveis (O que o modelo achou mais importante?)
importancias = pd.DataFrame({
    'Variavel': X.columns,
    'Importancia': modelo.feature_importances_
}).sort_values(by='Importancia', ascending=False)

print("\n🔥 --- VARIÁVEIS MAIS CRÍTICAS PARA PREVER O CALOTE ---")
print(importancias.to_string(index=False))
