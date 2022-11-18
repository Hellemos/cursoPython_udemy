'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
p1 = float(input("Qual o preço do produto 1?"))
p2 = float(input("Qual o preço do produto 2?"))
p3 = float(input("Qual o preço do produto 3?"))

if p1 <= 0 or p2 <= 0 or p3 <= 0:
    print("Por favor, digite um valor válido!")
elif p1 < p2 and p1 < p3:
    print("Melhor produto para compra é o produto com preço", p1)
elif p2 < p1 and p2 < p3:
    print("Melhor produto para compra é o produto com preço", p2)
elif p3 < p1 and p3 < p2:
    print("Melhor produto para compra é o produto com preço", p3)
