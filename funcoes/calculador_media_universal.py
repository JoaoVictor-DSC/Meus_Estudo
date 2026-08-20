import os
os.system("cls")

def calcular_media(lista_de_notas):
    total = 0  # 1. Cofrinho criado ANTES do laço
    
    for i in lista_de_notas:  # 2. Lendo diretamente os itens da lista
        total = total + i     # 3. Somando o valor no cofrinho
        
    # O laço terminou! Agora dividimos o total pela quantidade de itens
    media = total / len(lista_de_notas)
    return media

# --- SEU PROGRAMA PRINCIPAL ---
notas_semestre_1 = [7.3, 5.8, 9.2, 6.7]
notas_semestre_2 = [5.4, 6.7, 9.0, 6.0]

# Guardamos o retorno da função em variáveis
media_1 = calcular_media(notas_semestre_1)
media_2 = calcular_media(notas_semestre_2)

print(f"Média do 1º Semestre: {media_1}")
print(f"Média do 2º Semestre: {media_2}")