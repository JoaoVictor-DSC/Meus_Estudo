import os
os.system("cls")

def calcular_total(lista_de_precos):
    soma = 0
    
    for i in lista_de_precos:
        soma = soma + i
    return soma


Catalogo = {"varinha": 150.0,
            "capa": 85.5,
            "anel": 500.0
            }

carrinho = []

while True:
    pergunta = input("Qual item você quer comprar? (Digite 'sair' para finalizar): ")


    if pergunta in Catalogo:
        carrinho.append(Catalogo[pergunta])
        print("Item adicionado ao carrinho!")
    elif pergunta == "sair":
        break
    else:
        print("Item indisponível!")

    
total_pagar = calcular_total(carrinho)

print(f"Total a pagar: {total_pagar}")