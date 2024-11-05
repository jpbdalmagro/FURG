celsius = 0
faren = 0

escolha = input("Quer converter para qual escala? (F ou C) : ")

if 'F' in escolha:
	celsius = float(input("Digite a temperatura em C°: "))
	faren = (celsius * 9 / 5) + 32
	print(f"A temperatura em F° é {round(faren, 1)}")   
if 'C' in escolha:
	faren = float(input("Digite a temperatura em F°: "))	
	celsius = (faren - 32) / 9 * 5 
	print(f"A temperatura em C° é {round(celsius, 1)} ")
if not 'CF' in escolha:
	print("Não consigo converter para essa escala")
 
