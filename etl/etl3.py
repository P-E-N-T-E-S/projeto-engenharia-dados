import pandas as pd
from sqlalchemy import create_engine, text

usuario = 'usuario'
senha = 'senha'
host = 'localhost'
porta = '5434'
banco = 'estudantes'

engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

sql_mv = """
CREATE MATERIALIZED VIEW IF NOT EXISTS estudantes_mv AS
SELECT age, mental_health_rating, part_time_job, diet_quality, exam_score, attendance_percentage FROM estudantes;
"""

with engine.begin() as conn:
    conn.execute(text(sql_mv))

consulta_sql = "SELECT * FROM estudantes_mv;"

df = pd.read_sql(consulta_sql, engine)

df.to_csv('../staging/trust/resultado_consulta.csv', index=False)
