#Leia uma palavra e a transforme em uma senha
import random

random.seed()

letras = []
pos = []
anagrama = ''
cont = 0

nome = str(input("Digite um nome: ")).strip()

for letra in nome:
    letras.append(letra)
    while True:
        num = random.randint(0, len(nome) * 2 - 1)
        if num not in pos:
            break
    pos.append(num)
