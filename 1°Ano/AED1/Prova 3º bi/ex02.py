def extenso(data, cidade):
    dia, mes, ano = map(int, data.split('/'))
    
    if dia == 1:
        dia = '1°'
        
    return f"{cidade}, {dia} de {meses[mes - 1]} de {ano}."
    


meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

data = input("data no formato dd/mm/aaaa: ")
cidade = input("nome da cidade: ")

print(extenso(data, cidade))
