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
# import tkinter as tk
# from tkinter import messagebox

# def qualidade():
    
#     primeira_nota = int(informacao_primeira_nota.get())
#     segunda_nota = int(informacao_segunda_nota.get())
#     terceira_nota = int(informacao_terceira_nota.get())
   
#     if primeira_nota ==  (""):
#         messagebox.showwarning("Aviso!", "Por favor digite o número de peças produzidas")

#     else:
#         calculo_final = (primeira_nota + segunda_nota + terceira_nota)/3
#         messagebox.showinfo("Resposta", f"Sua nota em média Aritimétrica é\n{calculo_final}")


# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("400x500")


# # Labels
# lbl_mensagem_primeira = tk.Label(janela_principal, text="Digte a nota da primeira inspeção")
# lbl_mensagem_primeira.grid(row=1, column=0, pady=10, padx=10)

# lbl_mensagem_segunda = tk.Label(janela_principal, text="Digte a nota da segunda inspeção")
# lbl_mensagem_segunda.grid(row=3, column=0, pady=10, padx=10)

# lbl_mensagem_terceira = tk.Label(janela_principal, text="Digte a nota da terceira inspeção")
# lbl_mensagem_terceira.grid(row=5, column=0, pady=10, padx=10)


# # Entrys
# informacao_primeira_nota = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# informacao_primeira_nota.grid(row=2,column=0,pady=10,padx=10)

# informacao_segunda_nota = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# informacao_segunda_nota.grid(row=4,column=0,pady=10,padx=10)

# informacao_terceira_nota = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# informacao_terceira_nota.grid(row=6,column=0,pady=10,padx=10)


# # Button

# btn_enviar_mensagem_pecas = tk.Button(janela_principal, text="Enviar Mensagem", command=qualidade)
# btn_enviar_mensagem_pecas.grid(row=8, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=9, column=0, pady=10, padx=120)
                       
# # Rodar interface

# janela_principal.mainloop()

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def temperatura():
    
#     temperatura_informacao = int(informacao_temperatura.get())
  
#     if temperatura_informacao  <40:
#        messagebox.showwarning("Atenção", "Baixa carga!")
    
#     elif temperatura_informacao >40 or temperatura_informacao <70:
#         messagebox.showinfo("Atenção","Normal")

#     else:
#         messagebox.showinfo("Atenção","ALERTA: Resfriamento ativado!")
    

# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("400x250")


# # Labels
# lbl_mensagem_temperatura = tk.Label(janela_principal, text="Digte a temperatura")
# lbl_mensagem_temperatura.grid(row=1, column=0, pady=10, padx=10)

# # Entrys
# informacao_temperatura = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# informacao_temperatura.grid(row=2,column=0,pady=10,padx=10)


# # Button

# btn_enviar_mensagem_pecas = tk.Button(janela_principal, text="Enviar Mensagem", command=temperatura)
# btn_enviar_mensagem_pecas.grid(row=8, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=9, column=0, pady=10, padx=120)
                       
# # Rodar interface

# janela_principal.mainloop()

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox

# def clasificacao():
    
#     produto_clasificado = clasificando_produto.get()
 
   
#     if produto_clasificado ==  ("A"):
#         messagebox.showwarning("Informação", "O produto clasificado é um Alimento")

#     elif produto_clasificado == ("E"):
#         messagebox.showwarning("Informação", "O produto clasificado é Eletrônico")

#     else:
#         messagebox.showinfo("Informação", "O produto clasificado é desconhecido")


# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("400x250")


# # Labels
# lbl_mensagem_produto = tk.Label(janela_principal, text="Digte a nota da primeira inspeção")
# lbl_mensagem_produto.grid(row=1, column=0, pady=10, padx=10)

# # Entrys
# clasificando_produto = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# clasificando_produto.grid(row=2,column=0,pady=10,padx=10)

# # Button

# btn_enviar_mensagem_pecas = tk.Button(janela_principal, text="Enviar Mensagem", command=clasificacao)
# btn_enviar_mensagem_pecas.grid(row=8, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=9, column=0, pady=10, padx=120)
                       
# # Rodar interface

# janela_principal.mainloop()

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox, ttk


# def maquina():
#     sensor_porta = informacao_sensor.get()
#     botao_emergencia = informacao_emergencia.get()


#     if sensor_porta == "FECHADO":
#         messagebox.showwarning("Aviso!", "O sensor está fechado!, deixe ele aberto para proseguir")
    
#     elif  botao_emergencia == "LIGADO":
#         messagebox.showwarning("Aviso!", "O botão de emergencia está ativado!, desative para proceguir")
    
#     else:
#         messagebox.showinfo("Concluido!","Máquila ligada!, pronto para inspeção")
    
    

# # Criar Janela
# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("470x200")


# # Labels
# lbl_mensagem_sensor = tk.Label(janela_principal, text="Informação do sensor")
# lbl_mensagem_sensor.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem_emergencia = tk.Label(janela_principal, text ="Botão de emergencia")
# lbl_mensagem_emergencia .grid(row=2, column=0, pady=30, padx=10)


# # Componentes de ComboBox
# informacao_emergencia = tk.ttk.Combobox(janela_principal, values=["LIGADO","DESLIGADO"], width=30)
# informacao_emergencia.grid(row=2, column=1, pady=10, padx=10)

# informacao_sensor = tk.ttk.Combobox(janela_principal, values=["ABERTO", "FECHADO"], width=30)
# informacao_sensor.grid(row=0, column=1, pady=10, padx=10)


# # Button
# btn_enviar_mensagem = tk.Button(janela_principal, text="Enviar Mensagem", command=maquina)
# btn_enviar_mensagem.grid(row=3, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=3, column=1, pady=10, padx=120) 


# # Rodar interface
# janela_principal.mainloop()

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# import tkinter as tk
# from tkinter import messagebox

# def verificar():
#     total = int(tudo_total.get())
#     defeituosas = int(pecas_defeituosas.get())

#     porcentagem = (defeituosas / total) * 100

#     if porcentagem > 5:
#         resultado = "Revisar Processo"
#     else:
#         resultado = "Processo Otimizado"

#     messagebox.showinfo("Resultado", resultado)

# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("300x200")

# tk.Label(janela, text="Total de peças").pack()
# tudo_total = tk.Entry(janela)
# tudo_total.pack()

# tk.Label(janela, text="Peças defeituosas").pack()
# pecas_defeituosas = tk.Entry(janela)
# pecas_defeituosas.pack()

# tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

# janela.mainloop()

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# import tkinter as tk
# from tkinter import messagebox

# def medida():
    
#     peca_medida = float(informacao_medida_pega.get())
  
#     if peca_medida >9.8 and peca_medida <10.2:
#        messagebox.showwarning("Aviso!", "A peça está dentro da tolerância")
    
#     elif peca_medida <9.8:
#         messagebox.showwarning("Aviso!", "A peça está abaixo da tolerância")
    
#     else:
#         messagebox.showinfo("Aviso!", "A peça está acima da tolerância")
    

# janela_principal = tk.Tk()
# janela_principal.title("Janela princípal")
# janela_principal.geometry("400x250")


# # Labels
# lbl_mensagem_temperatura = tk.Label(janela_principal, text="Digte a Medida da peça")
# lbl_mensagem_temperatura.grid(row=1, column=0, pady=10, padx=10)

# # Entrys
# informacao_medida_pega = tk.Entry(janela_principal, font=("Arial", 12), width=20)
# informacao_medida_pega.grid(row=2,column=0,pady=10,padx=10)


# # Button

# btn_enviar_mensagem_pecas = tk.Button(janela_principal, text="Enviar Mensagem", command=medida)
# btn_enviar_mensagem_pecas.grid(row=8, column=0, pady=20, padx=30)

# btn_clicar_fechar = tk.Button(janela_principal, text="Fechar Aplicativo", font=("Arial", 14), bg="#E24D4D" , fg="white", command=janela_principal.destroy)
# btn_clicar_fechar.grid(row=9, column=0, pady=10, padx=120)
                       
# # Rodar interface

# janela_principal.mainloop()


# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

# import tkinter as tk
# from tkinter import messagebox

# def iniciar_prensa():
#     contagem = ""

#     for i in range(10, 0, -1):
#         contagem += str(i) + "\n"

#     contagem += "Prensa Ativada!"

#     messagebox.showinfo("Contagem Regressiva", contagem)

# janela = tk.Tk()
# janela.title("Setup da Prensa")
# janela.geometry("300x150")

# tk.Button(
#     janela,
#     text="Iniciar Contagem",
#     command=iniciar_prensa
# ).pack(pady=10)

# tk.Button(
#     janela,
#     text="Fechar Janela",
#     command=janela.destroy
# ).pack(pady=10)

# janela.mainloop()