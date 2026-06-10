# # 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# # "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox, ttk


# def principal():
#     nome_operario = operario_nome.get()
#     turno_operario = operario_turno.get()


#     if nome_operario == "":
#         messagebox.showwarning("Aviso!", "Por favor digite seu Nome")
    
#     elif  turno_operario == "":
#         messagebox.showwarning("Aviso!", "Por favor digite seu Turno")
    
#     else:
#         messagebox.showinfo("Operador", f"{nome_operario}, registrado no turno {turno_operario}. Boa jornada")
    
    

# # Criar Janela
# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("470x200")


# # Labels
# lbl_mensagem_operario = tk.Label(janela_principal, text="Digite seu nome")
# lbl_mensagem_operario.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem_turno = tk.Label(janela_principal, text ="Selecione seu Turno")
# lbl_mensagem_turno.grid(row=2, column=0, pady=30, padx=10)


# # Entrys
# operario_nome = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# operario_nome.grid(row=0,column=1,pady=10,padx=10)


# # Componentes de ComboBox
# operario_turno = tk.ttk.Combobox(janela_principal, values=["A", "B", "C"], width=30)
# operario_turno.grid(row=2, column=1, pady=10, padx=10)

# # Button
# btn_enviar_mensagem = tk.Button(janela_principal, text="Enviar Mensagem", command=principal)
# btn_enviar_mensagem.grid(row=3, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=3, column=1, pady=10, padx=120) 


# # Rodar interface
# janela_principal.mainloop()

# # 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# # exiba quantas peças serão produzidas em um turno de 8 horas.
# import tkinter as tk
# from tkinter import messagebox

# def pecas():
    
#     pecas_feitas = int(finalizando_pecas.get())
   

#     if pecas_feitas == (""):
#         messagebox.showwarning("Aviso!", "Por favor digite o número de peças produzidas")

#     else:
#         calculo_final = pecas_feitas * 8
#         messagebox.showinfo("Resposta", f"Serão feitas aproximadamente feitas {calculo_final} em 8 Horas")


# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("400x250")



# # Labels
# lbl_mensagem_pecas = tk.Label(janela_principal, text="Digte quantas peças são feitas em 1 hora?")
# lbl_mensagem_pecas.grid(row=0, column=0, pady=10, padx=10)


# # Entrys
# finalizando_pecas = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# finalizando_pecas.grid(row=1,column=0,pady=10,padx=10)


# # Button

# btn_enviar_mensagem_pecas = tk.Button(janela_principal, text="Enviar Mensagem", command=pecas)
# btn_enviar_mensagem_pecas.grid(row=2, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=3, column=0, pady=10, padx=120)
                       
# # Rodar interface

# janela_principal.mainloop()

# # 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# # ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def psi():
#     pedido_psi = int(psi_final.get())

#     if pedido_psi == "":
#         messagebox.showwarning("Aviso!", "Por favor digite o número de psi que você deseja converter")
    
#     else:
#           calculo_final = pedido_psi * 14.5
#     messagebox.showinfo("Resposta", f" O psi que você deseja é {calculo_final:.2f}")

# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("400x250")


# # Labels
# lbl_mensagem_psi = tk.Label(janela_principal, text="Digite o número que você deseja converter em PSI")
# lbl_mensagem_psi.grid(row=0, column=0, pady=10, padx=10)


# # Entrys
# psi_final = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# psi_final.grid(row=1,column=0,pady=10,padx=10)


# # Button

# btn_enviar_mensagem_psi = tk.Button(janela_principal, text="Enviar Mensagem", command=psi)
# btn_enviar_mensagem_psi.grid(row=2, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=3, column=0, pady=10, padx=120)

# # Rodar interface
# janela_principal.mainloop()

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
import tkinter as tk
from tkinter import messagebox

def qualidade():
    
    primeira_nota = (informacao_primeira_nota.get())
    segunda_nota = (informacao_segunda_nota.get())
    terceira_nota = (informacao_tercira_nota.get())
   

    if primeira_nota == (""):
        messagebox.showwarning("Aviso!", "Por favor digite o número de peças produzidas")

    else:
        calculo_final = (primeira_nota + segunda_nota + terceira_nota + 3 /2)
        messagebox.showinfo("Resposta", f"Sua nota em média Aritimétrica é{calculo_final}")


janela_principal = tk.Tk()
janela_principal.title("Janela princípal")
janela_principal.geometry("400x500")



# Labels
lbl_mensagem_primeira = tk.Label(janela_principal, text="Digte a nota da primeira inspeção")
lbl_mensagem_primeira.grid(row=1, column=0, pady=10, padx=10)

lbl_mensagem_segunda = tk.Label(janela_principal, text="Digte a nota da segunda inspeção")
lbl_mensagem_segunda.grid(row=3, column=0, pady=10, padx=10)

lbl_mensagem_terceira = tk.Label(janela_principal, text="Digte a nota da terceira inspeção")
lbl_mensagem_terceira.grid(row=5, column=0, pady=10, padx=10)


# Entrys
informacao_primeira_nota = tk.Entry(janela_principal, font=("Arial", 12), width=20)
informacao_primeira_nota.grid(row=2,column=0,pady=10,padx=10)

informacao_segunda_nota = tk.Entry(janela_principal, font=("Arial", 12), width=20)
informacao_segunda_nota.grid(row=4,column=0,pady=10,padx=10)

informacao_tercira_nota = tk.Entry(janela_principal, font=("Arial", 12), width=20)
informacao_tercira_nota.grid(row=6,column=0,pady=10,padx=10)


# Button

btn_enviar_mensagem_pecas = tk.Button(janela_principal, text="Enviar Mensagem", command=qualidade)
btn_enviar_mensagem_pecas.grid(row=8, column=0, pady=20, padx=30)

btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
btn_clicar_fechar.grid(row=9, column=0, pady=10, padx=120)
                       
# Rodar interface

janela_principal.mainloop()
