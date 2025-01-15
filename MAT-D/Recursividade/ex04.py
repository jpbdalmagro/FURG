# Escreva uma função recursivapara calcular a soma dos dígitos de um número inteiro e positivo, onde o número é fornecido como parâmetro

def soma(n):
    if len(n) == 0:
        return 0
    
    return int(n[0]) + soma(n[1:])

n = input("Digite um número: ")
print(soma(n))
