# O algoritmo bag-of-words é uma representação simplificada usada no processamento de linguagem natural. Nesse modelo,
# um texto é representado como a bolsa de suas palavras, desconsiderando a gramática e até mesmo a ordem das palavras,
# mas mantendo a multiplicidade, ou seja, a quantidade de vezes que cada palavra aparece.
# Faça um programa em python que implemente o “bag-of-words”, contando quantas vezes cada palavra aparece em um texto 
# e após construa um gráfico com o resultado.

import matplotlib.pyplot as plt

texto = input("Digite um texto: ").split()

palavras = []
contagem = []

for palavra in texto:
    if palavra not in palavras:
        palavras.append(palavra)
        contagem.append(1)
    else:
        contagem[palavras.index(palavra)] += 1
        
for palavra in palavras:
    print(f"{palavra}: {contagem[palavras.index(palavra)]}")
