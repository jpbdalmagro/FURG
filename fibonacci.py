t1 = 0
t2 = 1
cont = 2

print("-"*30)
print(f"{'Sequência de Fibonacci':^30}")
print("-"*30)

num = int(input("Digite o valor do enésimo termo: "))

print(f"A sequência de Fibonacci até o {num}º termo é: ", end="")
print(t1, end=" ")

if num >= 2:
    print(t2, end=' ')

if num >= 3:
    while cont < num:
        t3 = t1 + t2
        print(t3, end=" ")
        t1 = t2
        t2 = t3
        cont += 1

print('')
