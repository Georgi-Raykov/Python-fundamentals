symbols = input().split()

n = int(input())

half_symbols = len(symbols) // 2

for _ in range(n):

    faro_list = []

    for i in range(half_symbols):
        faro_list.append(symbols[i])
        faro_list.append((symbols[i + half_symbols]))

    symbols = faro_list
print(symbols)