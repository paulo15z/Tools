import subprocess

def run_script(script_path):
    try:
        subprocess.run(["python3", script_path], check=True)
    except Exception as e:
        print(f"[!] Erro ao executar: {e}")
