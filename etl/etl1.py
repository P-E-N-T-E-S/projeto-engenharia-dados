import zipfile
import os
import subprocess

dataset = 'jayaantanaath/student-habits-vs-academic-performance'
zip_filename = 'student-habits-vs-academic-performance.zip'
extract_folder = '../staging/raw'

subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset])

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

os.remove(zip_filename)
