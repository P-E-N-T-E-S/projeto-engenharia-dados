import schedule
import time
import subprocess

def executar_rotina():
    scripts = ["etl1.py", "etl2.py", "etl3.py"]
    for script in scripts:
        print(f"Executando {script}...")
        resultado = subprocess.run(["python3", script])
        if resultado.returncode != 0:
            print(f"Erro ao executar {script}. Código: {resultado.returncode}")
            break
    print("Rotina concluída.\n")

schedule.every(15).minutes.do(executar_rotina)

print("Agendador iniciado. Aguardando execução...")

while True:
    schedule.run_pending()
    time.sleep(1)
