cont = 0

while cont < 100:
    if 10 <= cont <= 99:
        if '2' in str(cont) or '1' in str(cont):
            if cont % 3 == 0:
                print(cont)
    cont += 1