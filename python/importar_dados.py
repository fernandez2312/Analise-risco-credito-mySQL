import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 1. Conexão estruturada via SQLAlchemy
url_conexao = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="#titi2312@", 
    host="localhost",
    port=3306,
    database="banco_risco"
)

engine = create_engine(url_conexao)

# 2. Carregar arquivo de dados reais
caminho_csv = r"C:\Caminho\Ate\O\Seu\Arquivo\credit_risk_dataset.csv"
df = pd.read_csv(caminho_csv)

print("Carregando os dados para o MySQL... Aguarde alguns segundos.")

# 3. Ingestão otimizada no banco de dados relacional
df.to_sql(
    name='credit_risk_dataset', 
    con=engine, 
    if_exists='replace', 
    index=False, 
    chunksize=5000
)

print("🎉 Sucesso! Todas as 32.500+ linhas foram importadas para o MySQL!")
