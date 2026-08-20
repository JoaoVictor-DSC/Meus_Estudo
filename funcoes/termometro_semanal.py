# O Termômetro Semanal (Soma e Divisão)
# Esta é idêntica à questão da média do boletim, só muda a historinha! Você quer saber a temperatura média da sua cidade nos últimos dias.
# Crie uma função chamada calcular_temperatura_media(lista_de_temperaturas).
# Dentro dela, use o for e o acumulador para somar todas as temperaturas da lista.
# Fora do for (mas ainda dentro da função), crie uma variável media que recebe o total dividido pelo tamanho da lista (usando o len()).
# Dê um return nessa média.
# No programa principal, crie uma lista de temperaturas (ex: temperaturas = [28.5, 30.0, 31.5, 29.0]), chame a função passando essa lista, guarde o resultado e dê um print.

import os 
os.system("cls")

def calcular_temperatura_media(lista_de_temperaturas):
    total = 0

    for i in lista_de_temperaturas:
        total = total + i
    media = total / len(lista_de_temperaturas)
    return media

temperaturas = [28.5, 30.0, 31.5, 29.0]

resultado = calcular_temperatura_media(temperaturas)

print(f"Média de temperatura é igual a {resultado}")