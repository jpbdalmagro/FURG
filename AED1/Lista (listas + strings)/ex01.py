#Escreva um programa que leia uma lista de palavras do usuário e retorne outra lista contendo apenas as palavras com mais de 5 caracteres.

palavras = []
palavras_maior_5 = []

while True:
    palavra = str(input("Digite uma palavra: "))
    palavras.append(palavra)
    if len(palavra) > 5:
        palavras_maior_5.append(palavra)
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"Palavras digitadas: {palavras}")
print(f"Palavras com mais de 5 caracteres: {palavras_maior_5}")
