# # Manipulação de arquivos e texto
# manipular_texto = "  Python é Muito legal!  "
# print(manipular_texto.strip().upper()) # "PYTHON"
# print(manipular_texto.strip().lower()) # "python"
# print(manipular_texto.strip().startswith("A")) # "Começar com letra inicial"
# print(manipular_texto.strip().capitalize()) # "Letras Inicial"
# print(manipular_texto.strip().title()) # "Titulo"
# print(manipular_texto.strip().replace("","")) # "preencher vazios"
# print(manipular_texto.strip().split()) # "Separar palavras"

# #Exercicio 1
# #Crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba a frase
# #com as seguintes trasformações:
# # -deixe o texto em letras minúsculas
# frase_usuario = input("Digite uma frase:")
# print(frase_usuario.strip().lower())

# Manipulação de Arquivos:

# # Escrevendo
# with open ("notas.txt", "w", encoding="utf-8") as texto:
#     texto.write("Estudar Python hoje!")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estamos evoluindo")

# #lendo
# with open("notas.txt", "r" , encoding="utf-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# # Exemplo 1
# # crie um programa que leia o conteúdo de um arquivo de texto e conte quantaas vezes a palavra "python"
# # aparece no arquivo. exiba o resultado para o usuário.
# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON") # Contar a palavra "Python"
#     contagem = conteudo.lower().count("python")
#     print(f"A contagem de palavras {contagem} é de...")

# Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
print(os.getcwd())

print(os.listdir())
print(os.listdir("C:/Users"))

# Criar pastas
os.mkdir("jaco")

# Criar Arquivo
with open ("notas.txt", "w", encoding="utf-8") as texto:
    texto.write("Estudar Python hoje!")
    texto.write("\nLer sobre Clean Code.")
    texto.write("\n Estamos evoluindo")

# Renomear pastas
os.rename("jaco", "Minha_Pasta")

# Apagar pastas
os.rmdir("Minha_Pasta")

# Excluir arquivos
# os.remove("notas.txt")