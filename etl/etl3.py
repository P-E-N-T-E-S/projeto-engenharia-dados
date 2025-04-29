import pandas as pd
from sqlalchemy import create_engine

# Configuração do banco
usuario = 'usuario'
senha = 'senha'
host = 'localhost'
porta = '5434'
banco = 'estudantes'

# Cria a conexão
engine = create_engine(f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

# Escreva sua query
consulta_sql = "SELECT age, mental_health_rating, part_time_job, diet_quality, exam_score, attendance_percentage FROM estudantes;"

# Executa a consulta e transforma em DataFrame
df = pd.read_sql(consulta_sql, engine)

# Exporta para CSV
df.to_csv('../staging/trust/resultado_consulta.csv', index=False)
