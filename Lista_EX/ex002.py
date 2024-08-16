'''Faça um programa em python que pergunte ao usuário o seguinte:
A viagem custará menos de R$ 30?
- Terá Wifi?
- Terá piscina?
- Terá churrasqueira?
O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
- Deverá custar menos de R$ 30
- Tem que ter wifi e piscina
- Se não tiver wifi ou piscina, tem que ter churrasqueira'''


cont = 0

valor = int(input("Digite quanto custará a viagem: "))
wifi = str(input("Terá wifi? [S/N]: " )).strip().upper()[0]
piscina = str(input("Terá piscina [S/N]: ")).strip().upper()[0]

print("A viagem custa menos de R$30? ", end='')
if valor <= 30:
	print("SIM")
	cont += 1
else:
	print("NÃO")
print("Tem wifi e piscina? ", end='')
if wifi == 'S' and piscina == 'S':
	print("SIM") 
	cont += 1
else:
	print("NÃO")
	churrasqueira = str(input("Terá churrasqueira? [S/N]: ")).strip().upper()[0]
	print("Tem churrasqueira? ", end='')
	if churrasqueira == 'S':
		print("SIM")
		cont += 1
	else:
		print("NÃO")

if cont == 2:
	print("A viagem atende as regras pedidas.")
else:
	print("A viagem NÃO atende as regras pedidas.")
		
