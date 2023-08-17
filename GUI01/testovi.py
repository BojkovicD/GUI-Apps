import tkinter as tk

def otvori_drugi_meni():
    global drugi_prozor
    root.withdraw()  
    
    drugi_prozor = tk.Toplevel()
    drugi_prozor.title("Drugi meni")
    drugi_prozor.geometry("800x600")
    
   

    dugmeback = tk.Button(drugi_prozor, text="Vrati se", command=rootnazad, width=10, height=2, bg="blue", fg="white")
    dugmeback.grid(row=1, column=0, padx=10, pady=10)
def rootnazad():
    root.deiconify()
    drugi_prozor.destroy()

    
root = tk.Tk()
root.title("Application")
root.geometry("800x600")
root.configure(bg="lightgray")

def izlaz():
    root.destroy()

izlaz = tk.Button(root, text="EXIT", command=izlaz, width=10, height=2, bg="blue", fg="white")
izlaz.grid(row=1, column=0, padx=10, pady=10)

play = tk.Button(root, text="PLAY", command=otvori_drugi_meni, width=10, height=2, bg="blue", fg="white")
play.grid(row=0, column=0, padx=10, pady=10)



root.mainloop()