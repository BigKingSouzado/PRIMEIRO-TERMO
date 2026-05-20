#1. O Problema da Idade
#ERRO
# idade = input("Digite sua idade: ")
# if idade >= 18:
#     print("Você é maior de idade.")

#CERTO
# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")

#MELHORIA
# print("Verificador de idade")

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")

# else:
#     print("Você é menor de idade, espere chegar aos 18 para ser maior de idade")

#2. A Escrita Fiel
#ERRO
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

#CERTO
# nome = input("Qual é seu nome?:")
# print("Seja bem-vinda,", nome)

#MELHORIA
# print("Identificador")

# nome = input("Digite qual é seu nome?:")
# idade = int(input("Digite qual é sua idade?:"))
# print(f"Seja bem-vindo(a), {nome},de idade {idade}")

#3. Falta de Espaço
#ERRO
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#CERTO
# numero = 10
# if numero >= 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

#MELHORIA
# numero = int(input("Digite qual quer número inteiro:"))
# if numero >= 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# 4. Esquecimento Fatal
#ERRO
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

#CERTO
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

#MELHORIA
# print("Configuração do login do usuario")

# usuario = input("Digite um nome de usuario para ser o padrão do login:")

# confirmacao = input("Digite o nome de usuario")

# if confirmacao == usuario:
#     print("Usuario confirmado com sucesso")
# else:
#     print("Usuario digitado incorretamente")

# 5. Atribuição vs. Comparação
#ERRO
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

#CERTO
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# else:
#     print("Está tudo bem com o clima, não precisa levar guarda-chuva")

#MELHORIA
# print("Observador de clima")
# print("Tipos de climas:\n Ensolarado\n Chuvoso\n Nublado\n Tempestade")
# clima = input("Digite o clima que está agora, com as informações dadas a cima:")

# if clima == "Ensolarado":
#     print("O clima está limpo!, não precisa de guarda-chuva")
# elif clima == "Chuvoso":
#     print("O clima está com fortes chuvas, leve um guarda-chuva")
# elif clima == "Tempestade":
#     print("O clima está perigoso, recomenda-se não sair de casa")
# elif clima == "Nublado":
#     print("O clima está misto, leve um guarda-chuva para se precaver")
# else:
#     ("Aconteceu um error na digitação ou na informção do clima")

# 6. Misturando Alhos com Bugalhos
# ERRO
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# CORRETO
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos")

#MELHORIA
# print("Somativa de pontos de semestre")

# semestre1 = int(input("Digite os pontos do primeiro semestre:"))
# semestre2 = int(input("Digite os pontos do segundo semestre:"))
# total = semestre1 + semestre2
# print(f"Parabéns! Você conseguiu no ano {total} pontos")

# 7. A Ordem dos Fatores
#O sistema deve dar "Excelente" para notas 9 ou 10.
# ERRO

# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

#CORRETO
# nota = 9.5

# if nota <= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

#MELHORIA
# print("Identificador de aprovação")

# nota = int(input("Digite sua nota:"))

# if nota <= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")
# else:
#     print("error na digitação")