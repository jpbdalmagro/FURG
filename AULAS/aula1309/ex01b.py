#1.b Leia um nome e mostre um anagrama aleatório dele
import random

random.seed()

letras = []
pos = []
anagrama = ''

nome = str(input("Digite um nome: ")).strip()

for letra in nome:
    letras.append(letra)
    while True:
        num = random.randint(0, len(nome) - 1)
        if num not in pos:
            break
    pos.append(num)

for n in pos:
    anagrama += letras[n]

print(f"Um anagrama de {nome} é {anagrama}!")
