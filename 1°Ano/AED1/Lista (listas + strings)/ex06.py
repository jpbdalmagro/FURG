# Faça um programa que gerencie uma lista de times de futebol. Você precisa criar um programa que armazene uma lista de times de futebol.
# O programa deve permitir ao usuário adicionar novos times à lista, remover times existentes e exibir a lista completa de times. 
# Crie um menu em que o usuário fique escolhendo a opção desejada

times = []

while True:
    print("\n1 - Adicionar time")
    print("2 - Remover time")
    print("3 - Lista de times")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        time = str(input("Digite o nome do time: "))
        times.append(time)
        print(f"{time} adicionado.")
    elif opcao == 2:
        time = str(input("Digite o nome do time que deseja remover: "))
        if time in times:
            times.remove(time)
            print(f"{time} removido.")
        else:
            print(f"{time} não encontrado.")
    elif opcao == 3:
        if times:
            print(times)
        else:
            print("Nenhum time cadastrado.")
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")

print("Fim do programa.")
