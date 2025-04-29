import pandas as pd
from sqlalchemy import create_engine

def limparnulos(df, coluna):
    if df[coluna].dtype == "object":
        df[coluna].fillna(df[coluna].mode()[0], inplace=True)
    elif df[coluna].dtype == "float64" or df[coluna].dtype == "int64":
        df[coluna].fillna(df[coluna].median(), inplace=True)

df = pd.read_csv('../staging/raw/student_habits_performance.csv')

for coluna in df.columns:
     limparnulos(df, coluna)

usuario = 'usuario'
senha = 'senha'
host = 'localhost'
porta = '5434'
banco = 'estudantes'

engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

tabela = 'estudantes'

df.to_sql(tabela, engine, if_exists='replace', index=False)

