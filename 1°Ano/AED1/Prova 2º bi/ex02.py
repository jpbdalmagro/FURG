#beecrowd 1180

lower = ''

len_nums = int(input())

nums = list(map(int, input().split()))
nums = nums[:len_nums]

for n in nums:
    if not lower:
        lower = n
    else:
        if n < lower:
            lower = n

position = nums.index(lower)

print(f"Menor valor: {lower}")
print(f"Posicao: {position}")
