#1.a Leia duas palavras e escreva se elas são anagramas
palavras = []
contagem = []
anagrama = True

for n in range(0, 26):
    contagem.append(0)

for n in range(1, 3):
    palavras.append(str(input(f"Digite a {n}ª palavra: ")).strip().lower())

for letra in palavras[0]:
    i = ord(letra) - ord('a')
    contagem[i] += 1

for letra in palavras[1]:
    i = ord(letra) - ord('a')
    contagem[i] -= 1    

print(contagem)
for n in contagem:
    if n != 0:
        anagrama = False

if anagrama:
    print("É um anagrama!")
else:
    print("Não é um anagrama!")
