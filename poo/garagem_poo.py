import os
os.system("cls")

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f"Vrumm! O {self.marca} {self.modelo} {self.ano} está ligado!")

meu_carro = Carro("Chevrolet","Impala","1967")

meu_carro.ligar()

