import tkinter as tk
from tkinter import messagebox, ttk


def cadastro_conta():
    nome_usuario = usuario_nome.get()
    cadastro_cpf_usuario = usuario_cpf_usuario.get()
    cadastro_email_usuario = usuario_cadastro_email.get()
    naoaluno_aluno_usuario = usuario_nao_aluno.get()
    

    if nome_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite o nome da pessoa cadastrada!")
    
    elif cadastro_email_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite o email da pessoa cadastrada!")
    
    elif cadastro_cpf_usuario == "":
        messagebox.showwarning("Aviso!", "Por favor digite o cpf da pessoa cadastrada")

    else:
        messagebox.showinfo("Cadrasto feito com sucesso!", f" {nome_usuario}!, de {idade_usuario} anos logando no sistema!")
    

# Janela_principal

janela_inicial = tk.Tk()
janela_inicial.title("Cadastro do Usuário")
janela_inicial.geometry("600x700")

# Labels


