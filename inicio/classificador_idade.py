# 1. Classificador de Idade (Ingresso de Cinema)
# Crie um programa que peça a idade do usuário e determine o valor da entrada do cinema:

import os 
os.system("cls")

idade = int(input("Informe sua idade: "))


if idade <12:
    v_ingresso = 10.00
    f_etaria = "Infantil"
elif idade >=12 and idade <=17:
    v_ingresso = 15.00
    f_etaria = "Meia-entrada"
elif idade >=18 and idade <=59:
    v_ingresso = 30.00
    f_etaria = "Inteira"
else:
    v_ingresso = 0.00
    f_etaria = "Gratuito"

print(f"valor do ingresso: R${v_ingresso} reais({f_etaria})")
    
