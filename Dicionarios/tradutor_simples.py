# 3. O Tradutor Simples (Dicionário como Ferramenta)
# Crie um dicionário chamado cores onde as chaves são os nomes das cores em português (ex: "vermelho", "azul", "verde") e os valores são os nomes em inglês ("red", "blue", "green").
# Use o input() para perguntar ao usuário qual cor ele quer traduzir. Depois, use a palavra digitada pelo usuário como chave para buscar e imprimir a cor em inglês dentro do seu dicionário.

import os
os.system("cls")
 
cores = {"vermelho" : "red" ,
         "amarelo" : "yellow" ,
         "verde" : "green"

         }

cor_escolhida = input("Qual cor gostaria de traduzir? ")

if cor_escolhida in cores:
    resultado = cores[cor_escolhida]
    print(f"A tradução é: {resultado}")
else:
    print("Desculpe, ainda não conheço essa cor!")