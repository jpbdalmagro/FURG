# Escreva uma função recursivaretornar um valor inteiro e positivo em ordem reversa, onde o valor é fornecido como parâmetro

def inverte(n: int, tamanho: int):
    if tamanho == 0:
        return n
    else:
        return n % 10 * 10 ** tamanho + inverte(n // 10, tamanho - 1)
    
n = int(input("Digite um número: "))
print(inverte(n, len(str(n)) - 1))
