import tkinter as tk
from Utils.runner import run_script
scripts = [
    {"name": "Tabela ARP", "file": "Scripts/arp.py"},
    {"name": "Script 2", "file": "scripts/script2.py"},
    {"name": "Script 3", "file": "scripts/script3.py"},
    {"name": "Script 4", "file": "scripts/script4.py"},
]

def launch_gui():
    root = tk.Tk()
    root.title("Tool Box")
    root.geometry("600x400")
    root.configure(bg="black")

    def open_info():
        tk.messagebox.showinfo("Info", "Sistema de execução de scripts")

    tk.Button(root, text="MENU", width=10).place(x=20, y=20)
    tk.Button(root, text="INFO", width=10, command=open_info).place(x=500, y=20)

    for i, script in enumerate(scripts):
        tk.Button(
            root, text=script["name"], width=40,
            command=lambda path=script["file"]: run_script(path)
        ).place(x=150, y=80 + i*50)

    tk.Button(root, text="<", width=5).place(x=100, y=330)
    tk.Button(root, text=">", width=5).place(x=450, y=330)

    root.mainloop()
