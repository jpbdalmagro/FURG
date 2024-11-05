#Crie um programa em Pyhon que leia uma data (DD/MM/AAAA) e diga se a data é válida. 

print("Verificador de datas")
print("-" * 20)

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
print("-" * 20)

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
	if 31 >= dia >= 1:
			print(f"A data {dia}/{mes}/{ano} é válida!")
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
	if 30 >= dia >= 1:
			print(f"A data {dia}/{mes}/{ano} é válida!")
if mes == 2:
	if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:	
		if 29 >= dia >= 1:
			print(f"A data {dia}/{mes}/{ano} é válida!")
		else:
			print(f"A data {dia}/{mes}/{ano} é inválida!")
	else:
		if 28 >= dia >= 1:
			print(f"A data {dia}/{mes}/{ano} é válida!")
		else:
			print(f"A data {dia}/{mes}/{ano} é inválida!")
		
if not 13 > mes > 0:
	print(f"A data {dia}/{mes}/{ano} é inválida!")
	
