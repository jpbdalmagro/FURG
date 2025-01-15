# Achar o maior elemento de um vetor

def maior(vetor, tamanho):
    if tamanho == 1:
        return vetor[0]
    else:
        return max(vetor[tamanho-1], maior(vetor, tamanho-1))
    
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(maior(vetor, len(vetor)))
