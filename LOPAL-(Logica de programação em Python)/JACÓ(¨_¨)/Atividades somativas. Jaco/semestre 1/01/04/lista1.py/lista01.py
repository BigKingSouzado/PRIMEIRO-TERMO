# 1. Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"

# print("Registros de veículo")
# modelo = input("Digite o modelo do seu veículo:")
# placa = input("Digite a Placa do seu carro:")

# print(f"veículo {modelo} de placa {placa} registrado com sucesso. Boa viagem!")

# 2. Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque
# cheio.

# print("Cálculo de gasto de gasolina por distancia")

# cpcd = float(input("Digite qual é a capacidade do tanque do combustível (em litro):"))
# cmdckml = float(input("Digite o consumo médio do caminhão por (km/L):"))
# total = cpcd / cmdckml

# print(f"A distância total que o veículo pode percorrer com o tanque cheio é: {round(total,2)}Km/h")

# 3. Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.

# print("Conversor de Moeda de Real(BRL) para Dólar(USD)")
# print("Taxa de conversão = 1 Dólar")
# print("Dólar 1 = 5,18")


# dolar = float(input("Digite qualtos Reais você deseja converter em Dólar:"))
# total = dolar / 5.18

# print("O total de Dólar convertido é:", round(total,2))

# # 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# # realizadas por um motorista.
# # ○ Exiba a média aritmética simples do tempo dessas entregas.

# print("Calculo de tempo em entregas de média aritmética")

# rota1 = float(input("Digite o tempo de entrega da rota1(em horas):"))
# rota2 = float(input("Digite o tempo de entrega da rota2(em horas):"))
# rota3 = float(input("Digite o tempo de entrega da rota3(em horas):"))

# total = (rota1 + rota2 + rota3) / 3
# print(f"A média aritmética do tempo da entregas(em horas) é:", round(total,2))


# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

# print("Monitor de carga")

# peso = int(input("Digite o peso atual do caminhão(em toneladas):"))
# if peso > 10:
#     print("Carga leve")
# elif 10 < peso < 25:
#     print("Carga padrão")
# else :
#     print("ALERTA!: Excesso de Peso!") 


# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".


# print("Classificador de Destino de carga")
# print("Código da carga\n N = Norte \n S = Sul\n Qualquer outro código é Internacional")

# codigo = input("\n Digite o Código da carga:")

# if codigo == "N":
#     print("Região Norte")
# elif codigo == "S":
#     print("Região Sul")
# else: 
#     print("Região Internacional")


# 7. Liberação de Saída: caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# print("Liberação de Saída")
# print("O motoristo só vai ser liberado se as informações estiverem completas")
# motorista = input("Digite (sim) se o motorista foi identificado:")
# checklist = input("Digite (concluido) se ele fez o checklist:")

# if motorista == "sim" and checklist == "concluido":
#     print("Autorização confirmada! o veículo está autorizado a iniciar a rota, Boa viagem")
# else:
#     print("O motorista não foi altorizado! ele não tem permição de iniciar a rota, tente novamente")

# 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# -Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".

# print("Cálculo de Atrasos")
# agendadas = int(input("Digite o total de entregas Agendadas:"))
# entregues = int(input("Digite o total de entregas Realizadas com atraso:"))
# total = agendadas + entregues
# porcentagem = total * 0.1

# if porcentagem > 10:
#     print("Necessário Otimizar rotas")
# else:
#     print("Logística Eficiente") 


# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

    
# print("Validação de Calibragem de pneu de carga")
# print("Um pneu de carga deve ter uma pressão entre 100 PSI e 110 PSI")
# calibragem = int(input("Digite o PSI do seu pneu:"))
# if calibragem < 100:
#     print("O pneu está abaixo do padrão recomendado")
# elif 100 < calibragem < 110:
#     print("O pneu está dentro do padrão")
# else :
#     print("O pneu está acima do padrão recomendado") 



# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

# print("Contagem de embarque")
# for embarque in range(5,1,-1):
#     print(f"Portão fechara em {embarque}")
# print("Portão trancado!")

# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

