# Implemente um programa em python que recebe um texto como entrada e realiza a seguinte análise:
# Conte e mostre o número total de caracteres no texto (incluindo espaços em branco).
# Conte e mostre o número total de palavras no texto.
# Conte e mostre o número total de frases no texto.
# Obs: considere que uma palavra é uma sequência de caracteres separada por espaços em branco e uma frase é uma sequência
# de palavras terminada por um ponto, ponto de exclamação ou ponto de interrogação .

texto = input("Digite um texto: ")

caracteres = len(texto)
palavras = texto.split(' ')
frases = 0

for palavra in texto:
    if palavra == '.' or palavra == '!' or palavra == '?':
        frases += 1
        
print(f"Total de caracteres: {caracteres}")
print(f"Total de palavras: {len(palavras)}")
print(f"Total de frases: {frases}")
