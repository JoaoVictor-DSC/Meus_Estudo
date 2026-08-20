# 3. Contagem Regressiva
# Peça ao usuário um número inteiro positivo N.
#  Use um laço de repetição para fazer uma contagem regressiva desse número até 1 e, ao final, exiba a mensagem "Decolar!".

import os 
import time
os.system("cls")

numero = int(input("Digite um número: "))
os.system("cls")

while numero > 0:
    print(numero)
    time.sleep(1)
    numero = numero - 1

os.system("cls")
print("Decolar 🚀")
