def lev(str_a, str_b):
    n = len(str_a)
    m = len(str_b)
    
    if m == 0:
        return n
    if n == 0:
        return m
    
    if str_a[n - 1] == str_b[m -1]:
        return lev(str_a[:-1], str_b[:-1])
    else:
        return 1 + min(lev(str_a, str_b[: -1]),
                       min(lev(str_a[:-1], str_b), 
                           lev(str_a[:-1], str_b[:-1])))
        

print(lev("prisco", "arisco"))
print(lev("cachorro", "cchorro"))
print(lev("case", "seca"))