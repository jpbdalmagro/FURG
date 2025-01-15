# Achar um elemento em um vetor ordenado de comprimento potência de 2

def busca(vetor, elemento, inicio, fim):
    meio = (inicio + fim) // 2
    if vetor[meio] == elemento:
        return meio
    if vetor[meio] < elemento:
        return busca(vetor, elemento, meio+1, fim)
    else:
        return busca(vetor, elemento, inicio, meio-1)
    
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
elemento = 7
print(busca(vetor, elemento, 0, len(vetor)-1))