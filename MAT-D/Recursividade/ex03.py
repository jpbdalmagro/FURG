# Escreva uma função recursiva para determinar se um vetor de inteiro é um palíndromo, onde o vetor e seu tamanho são fornecidos como parâmetro.

def palindromo(vetor, tamanho):
    if tamanho == 0 or tamanho == 1:
        return True
    if vetor[0] == vetor[tamanho-1]:
        return palindromo(vetor[1:tamanho-1], tamanho-2)
    else:
        return False
    
vetor = [1, 2, 3, 4, 3, 2, 1]

print(palindromo(vetor, len(vetor)))