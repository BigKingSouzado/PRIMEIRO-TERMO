# 1. o laço "for" (repetições determinados)
# use o "for" quando você sabe exatamnete quantas vezes algo deve 
# acontecer (como ler 10 sensores ou processar uma lista de peças).
# exemplo: relatório de produção díaria
# imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# #exeplo 1
# for lote in range(1,6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

# #exemplo 2
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# # exemplo 3
# # imagine o seguinte cenário, iremos produzir 20 discos de vinil
# for vinil in range(1,21):
#     print(f"produção de {vinil}, diária")
#     print("Qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

# exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento", "ParaFuso", "Martelo", "Prego", "chave de fenda", "Alicate"]
# tiposdepecas = ["Cilindrica", "Duplo", "Crônica", "prego", "orelha", "Redondo", "Phillips", "universal"]

# for item in pecas:
#     print(f"item em estoque: {item} e {tiposdepecas}")

# Exemplo 5
#imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção 
#você deseja e a partir da seleção ele listar os produtos

# print("Loja de vídeogame")
# print("Opções para escolher\n vídeogames dígite V\n Jogos dígite J")
# escolha = input("Digite sua opção:")

# if escolha == "V":
#     print("Você está na sessão de videogame")
#     videogame = ["Playstation 2", "Playstation 1", "Xbox 360", "GameCube"]
#     for videogame in videogame:
#         print(f"opções disponiveis de vídeogames:\n {videogame}")
    
    
# elif escolha == "J":
#     print("Você está na sessão de jogos")
#     games = ["God of war", "Resident Evil 4", "Halo 2", "Luigi's Mansion"]
#     for games in games:
#      print(f"opções disponiveis de Jogos:\n {games}")


# else:
#     print("opção errada")