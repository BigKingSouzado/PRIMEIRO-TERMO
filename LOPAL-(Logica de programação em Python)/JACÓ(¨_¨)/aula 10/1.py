# Tratamento de Erros e Depuração
# try e except são usaddos para lidar com erros de forma controlada,
# evitando que o programa quebre. O código dentro do bloco try é executado 
# normalmente, mas se ocorrer um erro, o controle é passado para o bloco
# except, onde podemos lidar com situação de forma apropriada.

# try:
#     numero = int(input("Digite um número: "))
#     resultado = 10/ numero
#     print("O resultado é:", resultado)

# except ValueError:
#     print("Erro: Você deve digitar um número válido")

# except ZeroDivisionError:
#     print("Erro: não é possível dividir por zero")

# except KeyboardInterrupt:
#     print("\n Programa interrrompido")

# except TypeError:
#     print("Erro: tipo de dado inválido.")

# except Exception as erro:
#     print("Erro inesperado:", erro)

#EXERCICIO 1
# Escreva um programa que solicite ao usúario calcule a média de três número. O programa deve
#lidar com possíveis erros, como a entrada de valores não numéricos ou a divisão por zero.

# try:

#     print("Somativa de 3 números")
#     numero1 = int(input("Digite o primeiro valor:"))
#     numero2 = int(input("Digite o segundo valor:"))
#     numero3 = int(input("Digite o terceiro valor:"))

#     total = (numero1 + numero2 + numero3 )/2

#     print("O resultado das três somativas foi",total)

# except  ValueError:
#     print("ERRO: Porfavor digite um número valído")


