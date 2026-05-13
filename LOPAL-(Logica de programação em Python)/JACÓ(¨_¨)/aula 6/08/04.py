#Questão 1

print("Registro de veículo")

modelo = input("Qual é o modelo do veículo?...")
placa = input("Qual é o placa do veículo?...")
print(F"Veículo {modelo} de placa {placa} registrado no sistema.Boa viagem!")

#Questão 2

print("Cálculo de autonomi")
tanque = float(input("Qual é a capacidade de seu tanque em litros"))
consumo = float(input("Digite o consumo médio por caminhão em km/l"))

total= tanque / consumo 
print(f"seu caminhão pode percorrer {total:.2f} em km/l")
print("seu caminhão pode percorrer", round(total,2), "em km/l")

#Questão 3

print("Conversor de moeda (frete internacional)")
valor_reais = float(input("Qual é o valor em reais que será convertido?..."))
taxa_dolar = float(input("Qual é o valor da taxa em do"))







#Questão 4

print("Média de entrega")
tempo1 = int(input("Qual foi o tempo para concluir a rota1 em horas"))
tempo2 = int(input("Qual foi o tempo para concluir a rota2 em horas"))
tempo3 = int(input("Qual foi o tempo para concluir a rota3 em horas"))

media = (tempo1 + tempo2 + tempo3) / 3
print = float(input("Qual é o peso atual do seu caminhão"))



#Questão 5

print("Monitor de carga")





# .lower = letra minuscula
# .upper = letra maiuscula
#Questão 6

print("Classificador de destino")
print("Regiões = N - Região Norte , S - Região Sul , Qualquer outra - Internacional")
regiao = input("Inserir o código da região: ").lower()
if regiao == "N".upper() or regiao == "n".lower():
    print("Regiaão norte")
elif regiao == "S":
    print("Região sul")
else:
    print("Região internacional")

#7 Questão
print("liberação de saída")
checklist = input|("O checklist foi concluido? [concluído ou não concluido]")
motorista = input("O motorista foi identificado? [sim ou não]")
if checklist == "Concluído" and motorista == "sim":
    print("veículo autorizado a iniciar a rota")
else:
    print("Veículo NÃo autorizado a iniciar a rota. verificar checklist e identificação do motorista")


# Questão 8

print("Cálculo de atrasos")
total_entregas = int(input("total"))


# Questão 9
print("Validação de calibragem")



# Questão 10
print("Contagem de embarque")
import time
for contagem in range(5,0,-1):
    time.sleep(1)
    print(contagem)
print("Portão Trancado")



# Questão 11
print("Somatório de frete (acumulador)")
while True:
    valor = float(input("Valor do frete"))
    if valor == 0:
        total += valor
        print(f"Total acumulado {total} do frete")
    print("Fim do cálculo de fretes")

#Questão 12
print("Monitoramento de frota")
maior_km = 0
for frota in range(1, 6):
    km = float(input(f"Digite a quilometragem de veículo {frota}:"))
    if km > maior_km:
        maior_km = km
print(f"A maior quilometragem registrada é: {maior_km}km.")

#Questão 13


