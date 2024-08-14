x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

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
