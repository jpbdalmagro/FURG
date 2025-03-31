num_a = int(input())
num_b = int(input())
result = 0

while num_a >= 1:
    if num_a % 2 == 1:
        result += num_b
    num_a = num_a // 2
    num_b *= 2

print(result)  