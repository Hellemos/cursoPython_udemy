'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input(
    "Em que turno você estuda? \n*** Digite M-matutino ou V-vespertino ou N-noturno ***\n")

if turno == "M-matutino":
    print("Bom dia!")
elif turno == "V-vespertino":
    print("Boa tarde!")
elif turno == "N-noturno":
    print("Boa noite!")
else:
    print("Valor inválido!")
