# Faça um Programa que leia três números e mostre o maior e o menor deles.
maior = 0
menor = 0

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 and n1 < n3 and n2 < n3:
    menor = n1
    maior = n3
elif n1 > n2 and n1 > n3 and n2 > n3:
    maior = n1
    menor = n3
elif n2 > n1 and n2 > n3 or n2 < n1 and n2 > n3 and n1 < n3:
    maior = n2
    menor = n1

print(maior)
print(menor)


#print("Maior:", maior, "\nMenor:", menor)
