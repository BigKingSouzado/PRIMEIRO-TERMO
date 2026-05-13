# Exercicio 1
# tente criar um código que conte de 1 a 10, mas use o continue para não imprimir 
# o número 5 (simulando uma falha de sensor específica no item)

for sensor in range(1,11):
    if sensor ==5:
        print(f"sensor n°{sensor}com falha")
    print(f"sensor {sensor} sem falha")
    continue
print("fim!")

