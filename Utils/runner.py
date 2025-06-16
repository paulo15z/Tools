import subprocess
import os

def run_script(script_path):
    try:
        full_path = os.path.abspath(script_path)

        if not os.path.exists(full_path):
            print(f"[!] Arquivo não encontrado: {full_path}")
            return

        result = subprocess.run(["python3", full_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Erro ao executar: {e}")
    except Exception as e:
        print(f"[!] Erro inesperado: {e}")
