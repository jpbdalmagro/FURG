erro = True

while erro:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    erro = False
    if x <= 0 | y <= 0:
        print("Aceito somente números positivos!")
        erro = True
    else:
        if y > x:
            primo("O inicio não pode ser maior que o fim!")
            erro = True
            
print(f"Os números primos entre {x} e {y} são:")

while x <= y:
    teste = 2
    primo = True    
    while teste < x and primo:
        resto = x % teste
        if resto == 0:
            primo = False
        teste += 1
    if primo:
        print(x)
    x += 1
