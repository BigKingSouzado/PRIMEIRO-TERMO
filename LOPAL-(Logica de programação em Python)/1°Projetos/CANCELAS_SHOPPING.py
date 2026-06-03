# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado 
# As entrada deverão ser registradas por placa.
# 
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

# Passo 2:
# Verificar tempo de permanencia
# Valor a ser cobrado

# Passo 3:
# Saida como sera?
# Calcular tempo de permanencia
# Se for tag gerar na fatura da tag
# Pagar ticket
# Devolver ticket na saida

# Passo 4:
# Gerar relatorio de entradas e saidas
# Tratamento de Erros
# Revisão do código

import datetime
print("Estacionamento do Shopping:")
print("Preço do estacionamento\n1 Hora = 10,00\n")


import datetime

print("Estacionamento do Shopping:")
print("Preço do estacionamento\n1 Hora = 10,00\n")

tag = input("Digite Sim (S) ou Não (N) se você tem sem parar: ")

if tag == "S":
    print("Informações obtidas com sucesso! Tenha um bom dia")

elif tag == "N":
    veiculo = input("Digite qual é a placa do seu veículo: ")
    
    horario = datetime.datetime.now().strftime("%H:%M:%S")
    
    print("<<<Gerando Ticket>>>")
    print(f"Veículo de placa {veiculo}\nChegado em: {horario}\nTenha uma otima visita ")
    


else:
    print("Informação inválida! verifica se seu sem parar está funcionando ou se as informações permitidas foram respondidas corretamente ")



