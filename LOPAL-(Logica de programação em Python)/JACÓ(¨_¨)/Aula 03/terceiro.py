# LOGICA E DECISOES
# SE CONDIÇÃO VERDADEIRA (if)
# SE CONDIÇÃO AINDA VERDADEIRA POREM COM CRITERIOS (elif)
# SENAO CONDIÇÃO FALSA (else)
# if elif e else
# sinais de > (maior) < (menor) = (igual)

#EXEMPLO 1
# print("verificar idade")
# idade = int(input("digite sua idade"))

# if idade >= 18:
#     print("você é maior de idade")
# elif idade >= 16:
#     print("voce nao é de maior porem pode votar")
# else:
#     print("você não é de maior")



#EXEMPLO 2
#VALORES
# print("checar valores")
# valor = int(input("digite um valor:"))

# if valor > 100:
#     print("valores acima de 100")
#     print("o valor é", valor + 1)


# else:
#     print("valores abaixo de 100:")
#     print("o valor é", valor - 1)

#EXEMPLO 3 
#criar um algoritmo que permita escolher a opção que deseja
print("menu de opção")
print("escolha uma das opções abaixo")
print("Filme = F \n" "Série = S \n"  "digete qual quer outra coisa para sair")

escolha = input("Digite sua opção \n")

if escolha == "F":
    print("você escolheu filmes")
elif escolha == "S":
    print("você escolheu série")
else:
    print("você saiu do programa :( seu chato")
