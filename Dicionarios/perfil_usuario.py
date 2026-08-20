# O Perfil do Usuário (Criando e Acessando)
# Crie um dicionário chamado personagem com as seguintes chaves: "nome" (ex: Gandalf), "classe" (ex: Mago) e "nivel" (ex: 99). Em seguida, faça um print que use os valores do dicionário para formar uma frase.
# Exemplo de saída: "O personagem Gandalf é um Mago de nível 99."

import os
os.system("cls")

personagem = {
    "nome" : "Patolino",
    "classe" : "Mago Supremo",
    "nivel" : 999
 }

print(f"O personagem {personagem['nome']} é um {personagem['classe']} de nível {personagem['nivel']}.")