# Crie um programa em Python que leia o rendimento mensal do usuário,
# qual o modelo de imposto (sem correção/com correção das perdas no governo Bolsonaro) e retorne o quanto ele deve pagar de imposto.

salario = float(input("Digite seu salário: "))

def imposto_sem_correcao(salario):
    if salario <= 1903.98:
        return salario
    elif salario <= 2826.65:
        return salario - 142.80
    elif salario <= 3751.05:
        return salario - 354.80
    elif salario <= 4664.68:
        return salario - 636.13
    return salario - 869.36

def imposto_com_correcao(salario):
    if salario <= 2500.44:
        return salario
    elif salario <= 3712.16:
        return salario - 187.54
    elif salario <= 4926.14:
        return salario - 465.95
    elif salario <= 6125.99:
        return salario - 835.41
    return salario - 1141.71

salario_sem_correcao = imposto_sem_correcao(salario)
salario_com_correcao = imposto_com_correcao(salario)

print(f"Seu salário sem correção: R$ {salario_sem_correcao:.2f}")
print(f"Seu salário com correção as perdas no governo Bolsonaro: R$ {salario_com_correcao:.2f}")
