# Faça um programa em python que leia uma frase e passe para maiúscula a primeira letra de cada palavra.
# Você não deve utilizar as funções prontas do python para converter para maiúscula ou minúscula.

frase = str(input("Digite uma frase: ")).strip()
frase = frase.split()
nova_frase = []

for word in frase:
    if ord(word[0]) >= 97 and ord(word[0]) <= 122:
        nova_frase.append(chr(ord(word[0]) - 32) + word[1:])
    else:
        nova_frase.append(word)

print(' '.join(nova_frase))
