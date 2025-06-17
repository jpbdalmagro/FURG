func = ''
maior_salario = 0
nome_maior_salario = ""
menor_salario = 0
nome_menor_salario = ""
soma_salarios = 0
cont = 0

while func != "fim":
    func = input("Digite o nome do funcionário: ").lower()
    if func != "fim":
        salario = float(input("Digite o salário do funcionário: "))
        if salario > maior_salario:
            maior_salario = salario
            nome_maior_salario = func.capitalize()
        if salario < menor_salario or cont == 0:
            menor_salario = salario
            nome_menor_salario = func.capitalize()
        soma_salarios += salario
        cont += 1

print(f"O funcionário com o maior salário é {nome_maior_salario} com o salário de R${maior_salario:.2f}")
print(f"O funcionário com o menor salário é {nome_menor_salario} com o salário de R${menor_salario:.2f}")
print(f"A média dos salários é R${soma_salarios / cont:.2f}")
