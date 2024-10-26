"""Leia uma senha e diga se ela é FORTE: 3 tipos, MÉDIA: 2 tipos, FRACA: 1 tipo, (NUMÉRICO, ALFABÉTICO, ESPECIAL)."""
verificadores = [False, False, False]
forca = 0

senha = str(input("Digite uma senha: ")).lower()

if senha:
    for char in senha:
        if ord('a') < ord(char) < ord('z'):
            verificadores[0] = True
        elif ord('0')< ord(char) < ord('9'):
            verificadores[1] = True
        else:
            verificadores[2] = True

    for verificador in verificadores:
        if verificador:
            forca += 1

    if forca == 1:
        print("Senha fraca!")
    elif forca == 2:
        print("Senha média!")
    else:
        print("Senha forte!")
else:
    print("Sua senha não pode ficar vazia!")
