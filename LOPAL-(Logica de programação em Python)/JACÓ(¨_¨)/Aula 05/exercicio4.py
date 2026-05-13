# Exercício 4 - identificar de peças defeituosas (for + if)
# percorra uma lista de medidas de peças:
# medidas = [50.1, 49.8, 52.0, 48.5]
# o padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais
# use um for para ler a lista e, para cada peça, diga se ela está "aprovado" ou "rejeitado"

pecas = [50.1, 49.8, 52.0, 48.5]
for medida in pecas:
    if medida >= 50.0:
        print(f"peça com medida {medida}mm: Aprovado")
    else:
        print(f"peça com medida {medida}mm: Rejeitado")
    