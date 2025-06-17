# Receba n números em uma lista e após separe os números em uma lista com positivos e uma com negativos

def separa_numeros(numeros: list, pos: list, neg: list):
    if not numeros:
        return  pos, neg 
    if numeros[0] > 0:
        pos.append(numeros[0])
        return separa_numeros(numeros[1:], pos, neg)
    neg.append(numeros[0])
    return separa_numeros(numeros[1:], pos, neg)


nums = []

while True:
    nums.append(int(input("Digite um número: ")))
    
    if nums[-1] == 0:
        print(separa_numeros(nums[:-1], [], []))
        break