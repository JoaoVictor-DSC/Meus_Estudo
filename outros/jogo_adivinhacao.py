import os
import random
os.system("cls")

numero_aleatorio = random.randint(1, 20)

while True:
    try:
        numero = int(input("Chute um número de 1 até 20: "))
        if numero > numero_aleatorio:
             print("O número secreto é menor. Tente de novo!")
        elif numero < numero_aleatorio:
             print("O número secreto é maior. Tente de novo!")
        else:
            print("Parabéns, você acertou!")
            break

    except ValueError:
        print("Digite somente números inteiros") 



