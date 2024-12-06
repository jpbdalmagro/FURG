"""Crie uma função que:
1) Recaba o estado e retorne o UF;
2) Receba o Uf e retorne o estado;
3) retorne os estados com maior e menor nome."""

with open("estados.csv", "r") as file:
    data = file.readlines()
    data = [line.strip().split(',') for line in data[1:]]
    
    
    def short_and_long(states: list) -> str:
        sizes = [len(state[1]) for state in states]
        longest, shortest = max(sizes), min(sizes)
        return states[sizes.index(longest)][1], longest , states[sizes.index(shortest)][1], shortest 
    
    
    longest_state, longest_size, shortest_state, shortest_size = short_and_long(data)
    
    
    def state_to_uf(search: str, states: list) -> str:
        for state in states:
            if state[1] == search:
                return state[2]
        else:
            return f"{search} não consta no banco de dados"
            
            
    def uf_to_state(search: str, states: list) -> str:
        for state in states:
            if state[2].strip() == search:
                return state[1]
        else:
            return f"{search} não consta no banco de dados"
    
    
    while True:
            
        print()
        print("Escolha uma opção")
        print("1 - Pesquisar por estado")
        print("2 - Pesquisar por UF")
        print("3 - Ver o nome mais curto")
        print("4 - Ver o nome mais comprido")
        print("5 - Sair")
        
        while True:
            choice = input("Digite a opção desejada: ")

            if choice in ['1', '2', '3', '4', '5']:
                break
            else:
                print("Opção inválida")

        print()

        if choice == '1':
            name = input("Digite o nome do estado: ").strip()
            uf = state_to_uf(name, data)
            print(f"O UF do estado {name} é{uf}.")
        elif choice == '2':
            uf = input("Digite o UF: ").upper()
            name = uf_to_state(uf, data)
            print(f"O estado com UF {uf} é o {name}.")
        elif choice == '3':
            print(f"O estado com nome mais curto é o {shortest_state} com {shortest_size} caracteres.")
        elif choice == '4':
            print(f"O estado com nome mais longo é o {longest_state} com {longest_size} caracteres.")
        else:
            break
    
    print("Tenha um bom dia!")
    