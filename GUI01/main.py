import tkinter as tk
from tkinter import ttk

def otvori_drugu_stranu():
    druga_strana = ttk.Frame(notebook)
    notebook.add(druga_strana, text="Druga strana")
    
    label = tk.Label(druga_strana, text="Ovo je druga strana", font=("Arial", 16))
    label.pack()

root = tk.Tk()
root.title("Application")
root.geometry("800x600")
root.configure(bg="lightgray")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

strana1 = ttk.Frame(notebook)
notebook.add(strana1, text="Prva strana")

izlaz = tk.Button(strana1, text="EXIT", command=root.destroy, width=10, height=2, bg="blue", fg="white")
izlaz.pack(padx=10, pady=10)

januar_label = tk.Label(strana1, text="Plata Januar:", width=20, height=2, font=("Arial", 13), bg="white", fg="black")
januar_label.pack(padx=10, pady=10)

rezultat_label = tk.Label(strana1, text="", width=20, height=2, bg="white", fg="black")
rezultat_label.pack(padx=10, pady=10)

januar_entry = tk.Entry(strana1, width=20, font=("Arial", 13), fg="black", bg="white")
januar_entry.pack(padx=10, pady=10)

dugme_ispis = tk.Button(strana1, text="UPIS", command=lambda: rezultat_label.config(text=januar_entry.get()), width=10, height=2, bg="blue", fg="white")
dugme_ispis.pack(padx=10, pady=10)

dugme_drugo = tk.Button(strana1, text="Promeni", command=otvori_drugu_stranu, width=10, height=2, bg="blue", fg="white")
dugme_drugo.pack(padx=10, pady=10)

root.mainloop()
