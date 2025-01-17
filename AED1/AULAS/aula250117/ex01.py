# Similaridade de string
def similaridade(strings: list, similar: int = 0):
    for _ in range(len(strings[0]) - len(strings[1])):
        strings[1] += '*'
    for i in range(len(strings[0])):
        if strings[0][i] == strings[1][i]:
            similar += 1
    return f"{pct(similar, len(strings[0]))}%"

def pct(similar: int, total: int) -> float:
    pct_similar = (similar * 100) / total
    return pct_similar

strings = [input(f"str:{i + 1}") for i in range(2)]
strings = sorted(strings, key=len)

print(similaridade(strings))
