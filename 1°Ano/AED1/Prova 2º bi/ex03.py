#beecrowd 3300

num = input()
num = [n for n in num]
sorte = True
one = False

for n in num:
    if one and int(n) == 3:
        sorte = False
    
    if int(n) == 1:
        one = True
    else:
        one = False
    
        
if sorte:
    print(f"{''.join(num)} NO es de Mala Suerte")
else:
    print(f"{''.join(num)} es de Mala Suerte")
    