#beecrowd 1581

casos = int(input())

for i in range(0, casos):
    idiomas = []
    cont = 0
    pessoas = int(input())
    for c in range(0, pessoas):
        idiomas.append(input())
    for idioma in idiomas:
        if idioma == idiomas[0]:
            cont += 1
    if cont == len(idiomas):
        print(idiomas[0])
    else:
        print("ingles")        
