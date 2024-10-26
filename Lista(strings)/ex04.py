# Escreva um programa que recebe uma frase do usuário e conta o número de palavras na frase.

frase = input("Digite uma frase: ")
palavras = frase.split(' ')

print(f"Total de palavras: {len(palavras)}")
