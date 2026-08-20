# 2. Lista de Compras (O comando .append())
# Crie um programa que comece com uma lista vazia compras = [].
#  Use um laço for com range(3) para perguntar ao usuário 3 produtos diferentes que ele deseja comprar.
#  Adicione cada produto digitado à sua lista usando o .append(). No final, imprima a lista completa.

import os
os.system("cls")

compras = []

for i in range(3):
    produtos = input(f"Qual o {i+1}º que deseja comprar: ")
    compras.append(produtos)

print(f"Seus Produtos: {compras}")