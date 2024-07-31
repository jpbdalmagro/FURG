nome = str(input("Digite seu nome: ")).strip().capitalize()
hora = int(input("Digite a hora do dia(sem os minutos): "))

if 0 <= hora <= 12:
	print(f"Bom Dia! {nome}.")
if 12 < hora <= 18:
	print(f"Boa Tarde! {nome}.")
if 18 < hora <= 23:
	print(f"Boa Noite! {nome}.") 

