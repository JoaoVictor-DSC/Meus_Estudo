# 6. O Fatorial de um Número
# O fatorial de um número $N$ (representado por $N!$) é a multiplicação de todos os inteiros de 1 até $N$ (exemplo: $5! = 1 \times 2 \times 3 \times 4 \times 5 = 120$).
#  Crie um programa que receba um número $N$ e calcule o seu fatorial usando um laço de repetição.

import os 
os.system("cls")

numero = int(input("Digite um número: "))
os.system("cls")
total = 1

for i in range(1, numero +1):
    total = total * i

print(f'{numero}! = {total}')
