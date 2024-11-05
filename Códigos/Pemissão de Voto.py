idade = int(input("Digite sua idade: "))

if idade >= 18:
	print("Já pode votar!")
	if 18 <= idade < 60:
		print("Voto obrigatório!")
	else:
		print("Voto facultativo!")
else:
	print("Não pode votar!")
