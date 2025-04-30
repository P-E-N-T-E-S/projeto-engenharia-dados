import pandas as pd
from sqlalchemy import create_engine, text

def clean_null(df, coluna):
    if df[coluna].dtype == "object":
        df[coluna].fillna(df[coluna].mode()[0], inplace=True)
    elif df[coluna].dtype == "float64" or df[coluna].dtype == "int64":
        df[coluna].fillna(df[coluna].median(), inplace=True)

df = pd.read_csv('../staging/raw/student_habits_performance.csv')

for coluna in df.columns:
     clean_null(df, coluna)

username = 'usuario'
password = 'senha'
host = 'localhost'
port = '5434'
database = 'estudantes'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

table = 'estudantes'

with engine.begin() as conn:
    conn.execute(text("DROP MATERIALIZED VIEW IF EXISTS estudantes_mv;"))

df.to_sql(table, engine, if_exists='replace', index=False)

