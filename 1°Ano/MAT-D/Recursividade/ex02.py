# Escreva uma função recursiva para computar a soma de todos os números de 1 a n, onde né fornecido como parâmetro

def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)
    
n = int(input("Digite um número: "))
print(soma(n))
