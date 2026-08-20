import os
os.system("cls")

class ContaBancaria:
    def __init__(self, titular):
        self.titular  = titular
        self.saldo  = 0.00

    def depositar(self,valor):
        self.saldo = self.saldo + valor
        print(f"deposito concluido, Saldo atual:{self.saldo:.2f}\n")

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        print(f"Saldo atual:{self.saldo}")

minha_conta = ContaBancaria("joão")

deposito = float(input("Quanto gostaria de depositar? "))
saque = float(input("Quanto gostaria de sacar? "))
os.system("cls")


minha_conta.depositar(deposito)
minha_conta.sacar(saque)
minha_conta.mostrar_saldo()


            
