import subprocess

def main():
    print("Executando comando ARP...\n")
    try:
        output = subprocess.check_output(["arp", "-a"], text=True)
        print(output)
    except Exception as e:
        print(f"Erro ao executar ARP: {e}")

if __name__ == "__main__":
    main()
