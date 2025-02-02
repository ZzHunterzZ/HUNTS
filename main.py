import tkinter as tk
from interface.interface import criar_interface

def main():
    janela = tk.Tk()
    janela.title("Processador de Arquivos .sor")
    janela.geometry("500x300")
    
    criar_interface(janela)
    
    janela.mainloop()

if __name__ == "__main__":
    main()
