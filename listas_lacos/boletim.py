# 3. O Boletim (Listas e Acumuladores)
# Crie a seguinte lista no seu código: notas = [7.5, 8.0, 6.5, 9.0]. 
# Usando um laço for para percorrer essa lista, some todas as notas em uma variável acumuladora (como você fez no exercício de 1 a N) e, no final, calcule e imprima a média dessas notas.

import os 
os.system("cls")

notas = [7.5, 8.0, 6.5, 9.0]
total = 0

for i in notas:
    total = total + i

media = total / len(notas)

print(f"Média = {media}")
