#Faça um programa em python em que o usuário digite uma lista de números inteiros (até digitar zero). 
#Após, o programa deve mostrar a frequência de cada número na lista, ou seja, quantos números 1 tem, quantos números 2, etc.

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
        for num in numeros:
            if n == num:
                cont += 1

        print(f"O número {n} aparece {cont} vezes.")
        cont = 0
