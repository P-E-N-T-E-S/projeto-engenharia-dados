import zipfile
import os
import subprocess

# Define o nome do dataset no Kaggle
dataset = 'shantanugarg274/sales-dataset'
zip_filename = 'sales-dataset.zip'
extract_folder = '../staging/raw'

# Faz o download usando o subprocess para chamar o comando
subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset])

# Extrai o arquivo zip
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print(f'Dataset baixado e extraído em: {extract_folder}')

os.remove(zip_filename)
