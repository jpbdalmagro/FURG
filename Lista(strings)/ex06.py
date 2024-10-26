# Escreva um programa em python que leia um texto e diga se é ou não um palíndromo
# (ou seja, se o inverso da string é igual a ela).
# Não será possível utilizar qualquer função no python que trabalhe com strings.

verificador = ''

print("-" * 30)
print(f"{'Verificador de palindromos':^30}")
print("-" * 30)
palindromo = str(input("Digite uma palavra ou frase: ")).lower()

if ' ' in palindromo:
    frase = palindromo.split()
    palindromo = ''
    for palavra in frase:
        palindromo += palavra

for i in range(len(palindromo) - 1, -1, -1):
    verificador += palindromo[i] 

if palindromo == verificador:
    print("\nIsso é um palindromo")
else: 
    print("\nIsso não é um palindromo")
    