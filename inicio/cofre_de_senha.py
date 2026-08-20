# 5. O Cofre de Senha
# Crie uma variável com uma senha secreta (por exemplo, 1234).
# Crie um programa com while que peça para o usuário digitar a senha.
# Se ele errar, exiba "Senha incorreta!" e peça novamente.
# O programa só deve parar quando a senha correta for digitada, exibindo "Acesso concedido!".

import os 
import time
os.system("cls")

senha_secreta = "1234"

while True:
    os.system("cls")
    senha_digitada = input("Digite sua senha: ")
    
    if senha_digitada == senha_secreta:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta!")
        time.sleep(1.5)

