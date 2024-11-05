from random import randint

tentativas = 0
palpite = 0
numero = randint(1, 1000000)

print("Vou pensar em um número entre 1 e 1.000.000. Tente adivinhar!")

while palpite != numero:
    palpite = int(input("Qual o seu palpite? "))
    if palpite < numero:
        print("Mais alto!")
        tentativas += 1
    if palpite > numero:
        print("Mais baixo!")
        tentativas += 1

print("Parabéns! Você acertou!")
print(f"Você precisou de {tentativas} tentativas para acertar.")