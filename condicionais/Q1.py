#Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
  print("%d é maior que %d" %(n1, n2))
elif n2 > n1:
  print("%d é maior que %d" %(n2, n1))
else:
  print("Os dois são iguais")
