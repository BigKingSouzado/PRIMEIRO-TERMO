# Exercicio 5 - uma balança industrial está pesando um lote de 6 sacos de insumos. 
# o peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# Crie um programa que peça ao usuário o peso de cada saco (via input dentro do loop) e, para cada um,
#informe se ele está "dentro do limite" (entre 48kg e 52kg) ou "fora do limite". no final, 
# exiba quantos sacos estão dentro do limite.

sacost = 0
for sacos in range(1,7):
    peso = float(input(f"Digite o peso do saco {sacos} em kg: "))
    if 48 <= peso <= 52:
      print(f"saco {sacos} com peso {peso}kg: Dentro do limite")  
    sacost += 1 #contra os sacos dentro do limite
else:
   print(f"Saco {sacos} com peso {peso}kg: Fora do limite")
print(f"Quantidade de sacos dentro do limite: {sacost}")