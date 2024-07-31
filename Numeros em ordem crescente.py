n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite um último número: "))

if n1 < n2:
	primeiro = n1
	segundo = n2
	if n1 < n3:
		if n3 < n2:
			segundo = n3
			terceiro = n2
		else:
			terceiro = n3
	else:
		primeiro = n3
		segundo = n1
		terceiro = n2
else:
	primeiro = n2
	segundo = n1
	if n2 < n3:
		if n3 < n1:
			segundo = n3
			terceiro = n1
		else:
			terceiro = n3
	else:
		primeiro = n3
		segundo = n2
		terceiro = n1

print(f"Os números em ordem crescente são {primeiro}, {segundo} e {terceiro}.")
