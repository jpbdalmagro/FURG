MULTIPLICAÇÃO(A, B)
    shift_a = 1
    total = 0
    for num in A
        mid = 0
        shift_b = 1
        for num_b in B
            mid = mid + ((num * shift_a) * (num_b * shift_b))
            shift_b = shift_b * 10
        total = total + mid
        shift_a = shift_a * 10
    return total

// Inicialização dos arrays A e B
A =
B =

// Inversão dos arrays A e B
A = Inverter(A)
B = Inverter(B)

// Chamada da função MULTIPLICAÇÃO e impressão do resultado
resultado = MULTIPLICAÇÃO(A, B)
print(resultado)
