# Interface gráfica com TKinter

# OS componentes principais (Widgets)
# TK: Janela principal
# label: é o texto a digitar = print
# Button: Botão clicável de evento 
# Entry: caixa de texto = input

# 0. Biblioteca
import tkinter as tk
from tkinter import messagebox

# 1. Criar janela
janela = tk.Tk()
janela.title("Minha primeira janela em GUI")
janela.geometry("800x600")

# 2. Criar função do botão
def mostrar_mensagem():
    messagebox.showinfo("")

# 3. Criar os componentes 
lbl_titulo_pagina = tk.Label(janela, text="Rockstargames", font=("Arial", 14, "bold"))
lbl_linha1_pagina = tk.Label(janela, text="red dead redemption 2", font=("Arial", 12, "bold"))
btn_clique_ativar = tk.Button(janela, text="GTA 6", font=("Arial", 14), bg="#2f02f7" , fg="white", command=mostrar_mensagem)
btn_clicar_fechar = tk.Button(janela, text="Fechar Aplicativo", font=("Arial", 14), bg="#f70202" , fg="white", command=janela.destroy)

lbl_titulo_pagina.grid(row=0, column=0, padx=10, pady=10)
btn_clique_ativar.grid(row=0, column=1, padx=10, pady=10)
btn_clicar_fechar.grid(row=0, column=2, padx=10, pady=10)

# 4. posicionar os componentes na janela
# lbl_titulo_pagina.pack(pady=20) #adiciona espaçamento
# btn_clique_ativar.pack(pady=30)
# btn_clicar_fechar.pack(pady=40)

# 5.Rodar Interface
janela.mainloop()