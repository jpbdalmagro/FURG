#Faça um programa em python que leia o nome de 4 times de futebol que estão em uma semifinal. Após, leia os gols das duas partidas: time1 x time2 e time3 x time4. Os times vencedores devem ir para
# a final. Caso haja empate, deve-se perguntar ao usuároi qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual time foi campeão. (Se empatar, perguntar quem foi o campeão)
print("Digite os 4 semifinalistas:"
		"\nTIME A X TIME B"
		"\nTIME C X TIME D")
time_a = str(input("\nTIME A: ")).strip()
time_b = str(input("TIME B: ")).strip()
time_c = str(input("TIME C: ")).strip()
time_d = str(input("TIME D: ")).strip()

print("\nOs jogos são:"
		f"\n{time_a} x {time_b}"
		f"\n{time_c} x {time_d}")

gols_a = int(input(f"\nQuantos gols o {time_a} fez: "))
gols_b = int(input(f"Quantos gols o {time_b} fez: "))
print("Jogo 1:"
		f"\n{time_a} {gols_a}x{gols_b} {time_b}")			

if gols_a == gols_b:
	print("\nA partida terminou empatada.")
	finalista = str(input("Quem se classificou? [A/B]: ")).strip().upper()
	if finalista == 'A':
		finalista_um = time_a
	if finalista == 'B':
		finalista_um = time_b
else:
	if gols_a > gols_b:
		finalista_um = time_a
	else:
		finalista_um = time_a
print(f"\n{finalista_um} se classificou!")

gols_c = int(input(f"\nQuantos gols o {time_c} fez: "))
gols_d = int(input(f"Quantos gols o {time_d} fez: "))
print("Jogo 2:"
		f"\n{time_c} {gols_c}x{gols_d} {gols_d}")
		
if gols_c == gols_d:
	print("\nA partida terminou empatada.")
	finalista = str(input("Quem se classificou? [C/D]: ")).strip().upper()
	if finalista == 'C':
		finalista_dois = time_c
	if finalista == 'D':
		finalista_dois = time_d
else:
	if gols_c > gols_d:
		finalista_dois= time_c
	else:
		finalista_dois = time_d
print(f"\n{finalista_dois} se classificou!")
		
print(f"\nA final vai ser entre {finalista_um} x {finalista_dois}")
gols_um = int(input(f"Quantos gols o {finalista_um} fez: "))
gols_dois = int(input(f"Quantos gols o {finalista_dois} fez: "))		

if gols_um == gols_dois:
	print("\nA partida terminou empatada.")
	campeao = str(input("Quem ganhou? [A/B]: ")).strip().upper()
	if finalista == 'A':
		campeao = finalista_um
	if campeao == 'B':
		campeao = finalista_dois
else:
	if gols_um > gols_dois:
		campeao = finalista_um
	else:
		campeao = finalista_dois
		
print(f"\n\nO {campeao} é o grande campeão!")

