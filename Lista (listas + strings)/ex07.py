# Faça um programa para reserva de ingressos de um cinema.
# O usuário pode escolher o lugar a ser reservado (fileira e a poltrona desejada - tamanho 10x10).
# Escreva um programa em Python que, através de um menu, permita ao usuário reservar ingressos,
# exibir a disponibilidade de lugares e exibir a lista de lugares reservados.

lugares = []
filas = []
fileiras = []
poltronas = []
reservado = []
cont = 0

for i in range(10):
    filas.append("O")
    fileiras.append(chr(i + 65))
    poltronas.append(str(i + 1))

for i in range(10):
    lugares.append(filas[:])

while True:
    print("\n1 - Reservar lugar")
    print("2 - Exibir disponibilidade de lugares")
    print("3 - Exibir lista de lugares reservados")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        fil = int(ord(input("Digite a fileira[A - J]:"))) - 65
        pol = int(input("Digite a poltrona[1 - 10]:"))
        if 0  <= fil < 10 and 1 <= pol <= 10:
            if lugares[fil][pol - 1] == 'O':
                lugares[fil][pol - 1] = 'X'
                print(f"{chr(fil + 65)}{pol} reservado.")
                reservado.append(f'{chr(fil + 65)}{pol}')
            else:
                print("Lugar já reservado!")
        else:
            print("Lugar inválido!")
    elif opcao == 2:
        print(poltronas)
        for f in lugares:
            print(fileiras[cont], end='')
            print(f)
            cont += 1
        cont = 0
    elif opcao == 3:
        if reservado:
            print(reservado)
        else:
            print("Nenhum lugar reservado!")
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")

print("Fim do Programa")
