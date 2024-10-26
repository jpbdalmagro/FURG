# Dada uma lista de números inteiros informada pelo usuário, escreva um programa em Python que conte quantos números únicos 
# (diferentes) estão presentes na lista. A digitação dos elementos da lista deve encerrar quando for digitado o número zero.

numeros = []
numeros_unicos = []
cont = 0

while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    numeros.append(n)

for n in numeros:
    if n not in numeros_unicos:
        numeros_unicos.append(n)
        cont += 1

print(f"Números digitados: {numeros}")
print(f"Números únicos: {numeros_unicos}")
print(f"Quantidade de números únicos: {cont}")
