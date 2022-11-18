# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []
count = 1

while count <= 3:
    n = int(input("Entre com os números: "))
    lista.append(n)
    count += 1
lista.sort(reverse=True)
print(lista)
