a = [9, 8, 1]
b = [1, 2, 3, 4]

a = a[::-1]
b = b[::-1]

def multi(a, b):
    shift_a = 1
    total = 0
    
    for num in a:
        mid = 0
        shift_b = 1
        for num_b in b:
            mid = mid + ((num * shift_a) * (num_b * shift_b))
            shift_b *= 10
        total += mid
        shift_a *= 10

    return total

print(multi(a, b))