# O Contador de Passos (Apenas Soma)
# Você tem um relógio inteligente que marca quantos passos você deu por dia.
# Crie uma função chamada somar_passos(lista_de_passos).
# Dentro dela, crie um acumulador (cofrinho), faça um laço for para percorrer a lista e somar todos os passos.
# No final da função, dê um return no total de passos.
# No programa principal, crie uma lista com os passos de 3 dias (ex: passos_da_semana = [3000, 5500, 4200]), passe ela para a sua função, guarde o resultado em uma variável e faça um print da resposta.

import os
os.system("cls")

def somar_passos(lista_de_passos):
    total_passo = 0

    for i in lista_de_passos:
        total_passo = total_passo + i
    return total_passo

passos_da_semana = [3000, 5500, 4200]

resultado = somar_passos(passos_da_semana)

print(f"quantidade de passos da semana foi = {resultado}")