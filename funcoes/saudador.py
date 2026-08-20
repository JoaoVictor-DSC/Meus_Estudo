# 1. O Saudador Automático (Parâmetros Básicos)
# Crie uma função chamada saudar(nome). Quando chamada, essa função não deve usar return, ela deve apenas dar um print em uma mensagem personalizada,
#  por exemplo: "Olá, [nome]! Seja muito bem-vindo(a)!".
# No programa principal, chame essa função 3 vezes passando nomes diferentes (ex: saudar("Ana"), saudar("Carlos")).

import os 
os.system("cls")

def saudar(nome):
    print(f"Olá, {nome}! Seja muito bem-vindo(a)!")

saudar("ana")
saudar("joão")
saudar("luiza")


