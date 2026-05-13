# Exercicio 3 - soma de cargas de energia (for)
# uma fábrica tem 5 máquinas. peça ao usuário (viva input dentro do loop)
# o consumo me kwh de cada uma das 5 máquinas. ao final do loop, o programa deve exibir o consumo total da fábrica
total = 0
for maq in range(1,6):
    maquina = float(input(f"Digite o consumo da maquina {maq} (em kmh)"))
    total += maquina
    print(f"O consumo total da fábrica é de {total} kmh")
    
