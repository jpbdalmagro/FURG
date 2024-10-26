# Faça um programa em python que:
# Crie uma senha aleatória de 6 caracteres alfanuméricos (A..Z,0..9);
# Descubra a senha criada (força bruta - tentar todas possibilidades). Obs: para encontrar a senha, 
# você não pode comparar pedaços da senha, precisa comparar toda senha (ex: if senha_gerada==senha_tentada: ).

from random import randint
from time import sleep

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
senha = ''
tentativa = ''
tentativas = 0

for i in range(6):
    if randint(0,1):
        senha += chr(randint(48,57))
    else:
        senha += chr(randint(65,90))
        
print(f"Senha gerada: {senha}")

sleep(1)

print("Descobrindo senha...")
for char1 in caracteres:
    for char2 in caracteres:
        for char3 in caracteres:
            for char4 in caracteres:
                for char5 in caracteres:
                    for char6 in caracteres:
                        tentativa = char1 + char2 + char3 + char4 + char5 + char6
                        tentativas += 1
                        if tentativa == senha:
                            break

print(f"Senha encontrada: {tentativa}")
print(f"Tentativas: {tentativas}")
