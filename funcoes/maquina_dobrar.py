# 2. A Máquina de Dobrar (O uso do return)
# Crie uma função chamada dobrar(numero). Essa função deve receber um número, multiplicá-lo por 2 e retornar o resultado usando return.
# No seu programa principal, peça para o usuário digitar um número, passe esse número para a sua função e imprima o resultado que ela te devolver.

import os
os.system("cls")

numero = int(input("Digite um número: "))

def dobrar(numero):
    dobro = numero * 2
    return dobro

resultado = dobrar(numero)
print(f"O dobro de {numero} é {resultado}")