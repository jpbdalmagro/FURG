s = m = 0

while m < 10:
    while s < 60:
        print(f"{m:02}:{s:02}")
        s += 1
    m += 1
    s = 0
print(f"{m:02}:{s:02}")