# 2. Calculadora de IMC (Índice de Massa Corporal)
# Peça ao usuário o peso (em kg) e a altura (em metros). Calcule o IMC dividindo o peso pela altura ao quadrado ($\text{peso} / \text{altura}^2$).

import os 
os.system("cls")

peso = float(input("Informe seu peso em kilos: "))
altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura ** 2)

if imc <18.5:
    status = "Abaixo do peso"
elif imc <24.9:
    status = "Peso normal"
elif imc <29.9:
    status = "Sobrepeso"
else:
    status = "Obesidade"

print(f"seu IMC é: {imc:.2f}({status})")
