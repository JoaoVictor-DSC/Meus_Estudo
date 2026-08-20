nota1 = float(input("INforme a 1ª nota: "))
nota2 = float(input("INforme a 2ª nota: "))
nota3 = float(input("INforme a 3ª nota: "))

soma_nota = nota1 + nota2 + nota3
media = soma_nota / 3


if media >= 7 and media <=10:
    resultado = "Aprovado"
elif media >= 5 :
    resultado = "Recuperação"
elif media >= 0:
    resultado = "Reprovado"
else:
    resultado = "Nota inválida"
    

print(resultado)
