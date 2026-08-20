import os
import time
os.system("cls")

while True:
    print("--------O MENU DO SISTEMA-------\n" \
    "Digite:\n [1] para Novo Cadastro\n [2] para Ver Cadastros \n [3] para Sair:\n")

    menu = int(input("Digite um número:"))
    os.system("cls")

    if menu == 1:
        try:
            print("-------CADASTRANDO USUÀRIO-------\n")
            nome = input("Digite o seu nome:")
            idade = int(input("Digite sua idade:"))

            with open("usuario_MENU.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nome} - {idade}\n")
                print("Dados salvos em cadastros.txt com sucesso!")
            

        except ValueError:
            print("Entrada inválida! Por favor,tente novamente")
            time.sleep(2)
            os.system("cls")

    elif menu == 2:
        try:
            print("-------USUÀRIOS CADASTRADOS-------\n")
            with open("usuario_MENU.txt", "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
                
    
        except FileNotFoundError:
            print("Nenhum usuário cadastrado!!")
            

    else:
        print("Encerrando programa!!")
        time.sleep(2)
        os.system("cls")
        break
            
