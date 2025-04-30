import pandas as pd
from sqlalchemy import create_engine, text

username = 'usuario'
password = 'senha'
host = 'localhost'
port = '5434'
database = 'estudantes'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

sql_mv = """
CREATE MATERIALIZED VIEW IF NOT EXISTS estudantes_mv AS
SELECT age, mental_health_rating, part_time_job, diet_quality, exam_score, attendance_percentage FROM estudantes;
"""

with engine.begin() as conn:
    conn.execute(text(sql_mv))

query = "SELECT * FROM estudantes_mv;"

df = pd.read_sql(query, engine)

df.to_csv('../staging/trust/resultado_consulta.csv', index=False)
