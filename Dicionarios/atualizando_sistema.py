# 2. Atualizando o Sistema (Modificando Dicionários)
# Crie um dicionário para um carro contendo apenas "marca" e "modelo".
# Em seguida, nas linhas de baixo:
# Adicione uma nova chave chamada "ano" com o valor 2024.
# Mude o valor da "marca" para outra marca de sua escolha.
# Imprima o dicionário inteiro no final para ver como ficou.

import os
os.system("cls")

Carro = {"marca":"Chevrolet ",
         "modelo":"Impala "
         }

Carro["marca"] = "Chevrolet "
Carro["modelo"] = "Impala  "
Carro["ano"] = "1967 "

print(f"O {Carro['marca']}{Carro['modelo']}{Carro['ano']}é um clássico da série Sobrenatural")