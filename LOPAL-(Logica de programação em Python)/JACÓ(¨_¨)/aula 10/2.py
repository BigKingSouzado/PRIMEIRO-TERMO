#Explicação de def: A palavra-chave "def" é usada para definir uma função em Python.
#Uma função eé um bloco de código reutilizável que realiza uma tarefa específica.
#Return: A palavra-chave "Return" é usada para finalizar a execução de uma função e retornar
#um valor para o local onde a função foi chamada.
#O valor retornado pode ser usado posteriormente no código.

# def nome_da_funcao(parametro1, parametro2):
#     # corpo de função (código que será executado)
#     resultado = parametro1 + parametro2
#     return resultado 

# # Exemplo 1:
# def saudacao(nome, idade):
#     nome = input("Digite seu nome: ")
#     return f"Olá, {nome}, {idade}!"
# print(saudacao("", 14))

# # Exemplo 2:
# def calcular_media(num1, num2, num3):
#     try:
#         media = (num1 + num2 + num3) / 3
#         return media
#     except TypeError:
#         return "Erro: Todos os valores devem ser números."
#     except ZeroDivisionError:
#         return "Erro: Não é possível dividir por zero"

# print(f"Calcular_media {(calcular_media(10, 20, 30))}")

# # Exemplo 3:
# def valores():
#     print("Digite Três valores:")
#     a = int(input("Digite o primeiro valor:"))
#     b = int(input("Digite o segundo valor:"))
#     c = int(input("Digite o terceiro valor:"))
#     return a, b, c
# print(f"O maior valor é: (max(valores()))")

# #Exemplo 4
# #Calcule o dobro de um número fornecido pelo usúario, tratamento erros de entrada ínvalida.
# def calcular_dobro():
#     try:
#         valor_digitado = int(input("Digitação o valor que deseja :"))
#         total_dobro = valor_digitado * 2
#         return total_dobro

#     except ValueError:
#         print("Digite um número válido")
# print(f"O calculo é: {calcular_dobro()}")
    

