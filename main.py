# App HUNTS (HUNTER + SOR)
# Copyright (C) 2024 [Seu Nome ou Nome da Organização]
#
# Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo
# sob os termos da Licença Pública Geral GNU conforme publicada pela Free Software Foundation,
# na versão 3 da licença, ou (a seu critério) qualquer versão posterior.
#
# Este programa é distribuído na esperança de que seja útil, mas SEM QUALQUER GARANTIA;
# sem sequer a garantia implícita de COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO FIM.
# Consulte a Licença Pública Geral GNU para mais detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com este programa.
# Se não, consulte <https://www.gnu.org/licenses/>.


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
