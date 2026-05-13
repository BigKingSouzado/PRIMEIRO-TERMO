# Exercício 2
# simule um semáforo com parada para cada cor. Determine um tempo que deseja
# para que quando muadr para tal cor ele  represente uma pausa para cada cor. use o continue
# para cada cor. use o continue para pular a cor amarela (simulando um semáfaro com defeito que não acenda a luz amarela
import time
semaforo = ["verde", "amarelo", "vermelho"]

for luz in semaforo:
     if luz == "amarelo":
        print(f"Aviso: luz {luz} do semáforo não está funcionando...")
        time.sleep(3)
        continue
print(f"luz {luz} do semáforo funcionando e ligada")
print("fim do ciclo do semáforo")
