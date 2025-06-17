def verifica_matriz(matriz):
    
    for linha in matriz[1:]:
        if len(linha) != len(matriz[0]):
            return 'Matriz Inválida'
    else:
        return 'Matriz Válida. O maior valor encontrado foi ' + maior_valor(matriz)
    
    
def maior_valor(matriz):
    vals = []
    
    for linha in matriz:
        for elemento in linha:
            vals.append(elemento)
            
    return str((max(vals)))


linhas = int(input("nº linhas: "))
matriz = []
print("valor vazio para pular linha")

for i in range(linhas):
    j = 0
    linha = []
    
    while True:
        valor = input(f"termo linha {i}, coluna {j}: ")
        
        if valor == '':
            break
        else:
            linha.append(int(valor))
            j += 1
    
    matriz.append(linha)
        
mensagem = verifica_matriz(matriz)

if len(matriz) == len(matriz[0]):
    mensagem += '. A soma da diagonal principal é ' + str(sum([matriz[i][i] for i in range(len(matriz))]))   
    
for i in matriz:
    print(i)
    
print(mensagem)