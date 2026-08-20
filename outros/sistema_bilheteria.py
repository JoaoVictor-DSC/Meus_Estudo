import os
os.system("cls")

def calcular_ingresso_total(lista_de_precos):
    soma = 0

    for i in lista_de_precos:
        soma = soma + i
    return soma

Filmes_cartaz = {"avatar": 30.0, 
                 "batman": 25.0, 
                 "matrix": 20.0 }

carrinho = []

while True:
    pergunta = input("Qual filme gostaria de assitir? ")
    if pergunta in Filmes_cartaz:
        carrinho.append(Filmes_cartaz[pergunta])
        print("INgresso guardado no carrinho!")
    elif pergunta == "sair":
        break
    else:
        print("Desculpe, esse filme não está em cartaz!!")


resultado = calcular_ingresso_total(carrinho)

os.system("cls")

if carrinho == []:
    print("Nenhum filme adicionado ao carrinho.")
else:
    print(f"valor total dos ingressos: {resultado}")