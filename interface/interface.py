
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



import customtkinter as ctk
from tkinter import filedialog, messagebox, PhotoImage
import ctypes
from processamento.conversor import processar_arquivos_sor  # Importa a função de conversão

# Configuração inicial
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")

# Criando a janela principal
root = ctk.CTk()
root.title("Processador de Arquivos OTDR")
root.geometry("700x500")
root.resizable(False, False)

# Definir o ícone da janela
root.iconbitmap("HUNTS.ico")  # Certifique-se de que o arquivo HUNTS.ico está na mesma pasta
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("HUNTS")
icon = PhotoImage(file="HUNTS.png")
root.tk.call("wm", "iconphoto", root._w, icon)

# Funções para seleção de arquivos e pastas
def selecionar_pasta(entrada_pasta):
    pasta = filedialog.askdirectory()
    if pasta:
        entrada_pasta.delete(0, "end")
        entrada_pasta.insert(0, pasta)

def selecionar_planilha(entrada_planilha):
    arquivo = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if arquivo:
        entrada_planilha.delete(0, "end")
        entrada_planilha.insert(0, arquivo)

def processar(entrada_pasta, entrada_planilha, var_sentido, botao_concluido):
    pasta = entrada_pasta.get()
    planilha = entrada_planilha.get()
    sentido = var_sentido.get()
    
    if not pasta or not planilha or not sentido:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    
    messagebox.showinfo("Processando", "Iniciando o processamento dos arquivos...")
    
    try:
        processar_arquivos_sor(pasta, planilha, sentido)
        messagebox.showinfo("Sucesso", "Processamento concluído com sucesso!")
        botao_concluido.configure(state="normal")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o processamento: {e}")

def cancelar():
    resposta = messagebox.askyesno("Cancelar", "Tem certeza que deseja cancelar?")
    if resposta:
        root.quit()

def concluir():
    resposta = messagebox.askyesno("Concluir", "Deseja realmente finalizar o programa?")
    if resposta:
        root.quit()

# Layout principal
frame_principal = ctk.CTkFrame(root)
frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

# Seleção de Pasta
ctk.CTkLabel(frame_principal, text="📂 Pasta de Arquivos", font=("Arial", 14)).pack()
entrada_pasta = ctk.CTkEntry(frame_principal, width=400)
entrada_pasta.pack(pady=5)
ctk.CTkButton(frame_principal, text="Selecionar", command=lambda: selecionar_pasta(entrada_pasta)).pack()

# Seleção de Planilha
ctk.CTkLabel(frame_principal, text="📊 Planilha Excel", font=("Arial", 14)).pack(pady=10)
entrada_planilha = ctk.CTkEntry(frame_principal, width=400)
entrada_planilha.pack(pady=5)
ctk.CTkButton(frame_principal, text="Selecionar", command=lambda: selecionar_planilha(entrada_planilha)).pack()

# Seleção do Sentido
ctk.CTkLabel(frame_principal, text="↔ Sentido do Troço", font=("Arial", 14, "bold"), text_color="white").pack(pady=10)
var_sentido = ctk.StringVar()
botao_frame = ctk.CTkFrame(frame_principal)
botao_frame.pack()
ctk.CTkButton(botao_frame, text="A → B", command=lambda: var_sentido.set("A-B"), width=100).pack(side="left", padx=20)
ctk.CTkButton(botao_frame, text="B → A", command=lambda: var_sentido.set("B-A"), width=100).pack(side="right", padx=20)

# Botões de ação
botoes_frame = ctk.CTkFrame(frame_principal)
botoes_frame.pack(pady=20)
botao_concluido = ctk.CTkButton(botoes_frame, text="🏁 Concluído", state="disabled", command=concluir)
ctk.CTkButton(botoes_frame, text="❌ Cancelar", fg_color="red", command=cancelar, width=120).pack(side="left", padx=10)
ctk.CTkButton(botoes_frame, text="✅ Processar", fg_color="green", command=lambda: processar(entrada_pasta, entrada_planilha, var_sentido, botao_concluido), width=120).pack(side="left", padx=10)
botao_concluido.pack(side="left", padx=10)

# Rodapé
rodape = ctk.CTkLabel(root, text="© 2024 Processador OTDR | Versão 1.0.0", font=("Arial", 10), text_color="gray")
rodape.pack(side="bottom", pady=10)

# Executar a interface
root.mainloop()
