#beecrowd 1332

def verifica(entrada: str) -> int:
    one = ['o', 'n', 'e']
    two = ['t', 'w', 'o']
    
    cont_one = 0
    cont_two = 0
    
    if len(entrada) <= 3:
        
        for i in range(len(entrada)):
            if entrada[i] == one[i]:
                cont_one += 1
            if entrada[i] == two[i]:
                cont_two += 1
        
        if cont_one >= 2:
            return 1
        elif cont_two >= 2:
            return 2
        
    else:
        return 3

cases = int(input())

for i in range(cases):
    fala = str(input()).lower()
    print(verifica(fala))
