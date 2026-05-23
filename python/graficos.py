import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 1. Conectar ao seu MySQL real com a senha certa
url_conexao = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="#Titi2312@", # Sua senha com o T maiúsculo
    host="localhost",
    port=3306,
    database="banco_risco"
)
engine = create_engine(url_conexao)

# 2. Puxar os dados direto para o Pandas
df = pd.read_sql("SELECT person_home_ownership, loan_status, loan_amnt FROM credit_risk_dataset WHERE person_age <= 80", engine)

# Traduzir os nomes para ficar bonito no portfólio nacional
df['person_home_ownership'] = df['person_home_ownership'].replace({
    'RENT': 'Aluguel', 'MORTGAGE': 'Financiada', 'OWN': 'Própria', 'OTHER': 'Outros'
})

# 3. Configurar o visual do gráfico (Estilo Executivo)
plt.figure(figsize=(10, 5))
sns.set_theme(style="whitegrid")

# Criar gráfico de barras mostrando a Taxa de Inadimplência por Tipo de Moradia
ax = sns.barplot(
    data=df, 
    x='person_home_ownership', 
    y='loan_status', 
    errorbar=None, 
    palette='Blues_r',
    edgecolor='black'
)

# Customizar títulos e legendas
plt.title('Taxa de Inadimplência por Tipo de Moradia do Cliente', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Tipo de Moradia', fontsize=12)
plt.ylabel('Taxa de Inadimplência (Média)', fontsize=12)

# Transformar o eixo Y em porcentagem limpa
import matplotlib.ticker as mtick
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

# Salvar a imagem do gráfico direto na pasta do seu projeto
plt.tight_layout()
plt.savefig('dashboard_risco_moradia.png', dpi=150)
print("🎉 Gráfico gerado e salvo com sucesso como 'dashboard_risco_moradia.png'!")
plt.show()
