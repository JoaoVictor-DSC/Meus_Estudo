# Para praticar o tratamento de erros antes de passarmos para a criação e leitura de arquivos, crie um pequeno script:
# Peça ao usuário para digitar o nome (texto) e a idade (número inteiro).
# O campo de idade deve estar protegido por um try / except dentro de um while True.
# Se ele digitar letras ou símbolos na idade, o programa deve exibir uma mensagem de erro e perguntar a idade novamente, até que ele digite um número inteiro válido.
# Quando a idade for válida, encerre a validação e exiba uma mensagem confirmando o cadastro (ex: "Usuário [Nome] de [Idade] anos cadastrado!").

import os
os.system("cls")

nome = input("Digite seu nome: ")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        print(f"Usuário {nome} de {idade} anos cadastrado!")
        break
    except ValueError:
        print("Entrada inválida! Por favor, use apenas números inteiros(ex: 15, 50, 65).\n")
        

with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome} - {idade}\n")
    print("Dados salvos em cadastros.txt com sucesso!")