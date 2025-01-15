# Escreva uma função recursiva para escrever em ordem os valores inteiros de xa y, onde xe ysão fornecidos como parâmetro.

def escreve(x, y):
    if x == y:
        print(x)
    else:
        print(x)
        escreve(x+1, y)
        
x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
escreve(x, y)