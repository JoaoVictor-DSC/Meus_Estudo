total_vogais = 0
frase = input("Informe uma palavra ou frase: ").lower()
vogais = "aeiou"

for letra in frase:   
    if letra in vogais:
        total_vogais= total_vogais + 1

print(f"Quantidade de vogais = {total_vogais}")

