"""Leia um string e verifiique se é um palindromo"""
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
