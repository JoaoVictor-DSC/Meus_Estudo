import random
numero_secreto = random.randint(1,50)

while True:
    resposta = int(input("Informe um número: "))

    if resposta > numero_secreto:
        print("Muito alto!")

    elif resposta < numero_secreto:
        print("Muito baixo!")

    else:
        print("Parabéns, você acertou!")
        break

    
