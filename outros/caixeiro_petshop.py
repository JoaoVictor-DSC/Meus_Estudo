import os 
os.symlink("cls")

def calcular_fatura_pet(lista_de_servicos):
    soma = 0

    for i in lista_de_servicos:
        soma =soma + i
    return soma

tabela_servicos = {"banho": 50.0,
                    "tosa": 40.0,
                    "vacina": 90.0,
                    "unha": 15.0}

servicos_escolhidos = []

while True:
    