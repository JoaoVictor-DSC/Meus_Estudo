n = int(input("Informe um número de repetições: "))
a=0
b=1

for i in range(n):
  print(f"{a}")
  proximo = a + b
  a = b
  b = proximo
