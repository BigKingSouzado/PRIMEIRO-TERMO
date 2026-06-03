# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para 
# cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino 
# da pessoa. O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador
# , e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até
#  que o usuário decida encerrar.

#LEVANTAMENTOS: 
# 1° identifica qual andar está
# 2° identificar quantos andares tem
# 3° chamar o elevador 
# 4° falar da capacidade máxima de 5 pessoas
# 5° O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando).
# 6° indicar que quando clicar no botão de saída o elevador vai abrir.

#Elevador de prédio
import time
andar_atual = 0

print("======= ELEVADOR ========")
print("======= ABRINDO =======")
print("*Capacidade máxima de pessoas 5*")
print("======= ANDARES =======\n0(Térreo)\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10(Terraço)")


andar_atual = int(input("Digite o número do andar que você está?:"))
print(f"O elevador está no andar {andar_atual}")

andar_desejado = int(input("Digite o número do andar que você deseja:"))

for andar in range(andar_desejado):
    if andar_atual < andar_desejado:
        time.sleep(1)
        print(f"Subindo Andar{andar_atual + 1}")
    
    elif andar_atual > andar_desejado:
        time.sleep(1)
        print(f"Desendo Andar{andar_atual - 1}")
      
    # else:
    #     print("Ouve um erro no elevador contate o suporte")




saida = input("Deseja abrir o elevador?\n Digite S(sim) N(não)\n")
# Fechando o elevador
print("Andar chegado com sucesso")
print("Cuidado ao sair do elevador")

for tempo in range(1,6):
    time.sleep(1)
    print(f"Fechando em {tempo}")

if saida == "N":
    print("")

elif saida == "S":
    print("======= FECHADO =======")
    
    
    
    
    
    
    
    
    
    
    
    
    
    # elif andares == andar_atual:
    #     time.sleep(1)
    #     print("Você já está no andar desejado")
    
    # elif andares == andar_atual:
    #     time.sleep(1)
    #     print(f"Desendo Andar{andar - 1}")
        
        
