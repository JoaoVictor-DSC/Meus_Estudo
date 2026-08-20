# 4. A Soma de 1 a N
# Peça ao usuário um número inteiro $N$. O programa deve usar um laço para somar todos os números inteiros de 1 até $N$ (exemplo:
#  se $N = 4$, o programa deve calcular $1 + 2 + 3 + 4 = 10$) e exibir o total no final.

import os
os.system("cls")

numero = int(input("Digite um número: "))
total = 0

for i in range(1, numero + 1):
    numero = numero - 1
    total = total + i
    print(f"{numero}")

print(f"Total: {total}")
