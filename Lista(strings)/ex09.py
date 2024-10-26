'''Faça um programa em python que leia três textos. O programa deve imprimir o primeiro texto substituindo todas as ocorrências do segundo 
    pelo terceiro. Não deve ser utilizada qualquer função no python que trabalhe com strings'''
    
texto = input("Digite o primeiro texto: ").split()
alvo = input("Digitea palavra a ser substituida: ")
substituto = input("Digite a palavra substituta: ")

for palavra in texto:
    if palavra == alvo:
        texto[texto.index(palavra)] = substituto

nova_frase = ' '.join(texto)
print(f"\nFrase alterada: {nova_frase}!")
