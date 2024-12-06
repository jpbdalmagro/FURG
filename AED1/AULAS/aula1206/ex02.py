"""Crie um código que 
1) Receba o código de estado e retorne quantas cidades há para aquele código;
2) Receba um string e retorne quais cidades contêm o string;
3) Quantas cidades tem o string no nome."""

with open('municipios.csv', 'r') as file:
    data = file.readlines()
    data = [line.strip().split(',') for line in data]
    
    
    def cities_in_state(code: str, cities: list) -> int:
        return sum([1 for city in cities if city[0] == code])
    
    
    def cities_with_str(string: str, cities: list) -> list:
        return [city[2] for city in cities if string in city[2]]
    
    
    def cities_with_str_ammount(string: str, cities: list) -> int:
        return sum([1 for city in cities if string in city[2]])
    
    while True:
        print()
        print("""1 - Quantidade de cidades por estado
2 - Cidades com string no nome
3 - Quantidade de cidades com string no nome
4 - Sair
--------------------------------------------""")
        
        while True:
            choice = input("Digite a opção desejada: ")
            
            if choice in ['1', '2', '3', '4']:
                break
            else:
                print("Opção inválida")
        
        if choice == '1':
            state_code = input("Digite o código do estado: ")
            cities_ammount = cities_in_state(state_code, data)
            print(f"O estado tem {cities_ammount} cidades.")
        elif choice == '2':
            str_to_search = input("Digite a string que deseja procurar: ")
            cities_list = cities_with_str(str_to_search, data)
            print(f"Essas são todas as cidades com {str_to_search} no nome:")
            for city in cities_list:
                print(city)
        elif choice == '3':
            str_to_search = input("Digite a string que deseja procurar: ")
            cities_ammount = cities_with_str_ammount(str_to_search, data)
            print(f"A quantidade de cidades com {str_to_search} no nome é {cities_ammount}")
        else: 
            break
        
    print("Tenha um bom dia!")