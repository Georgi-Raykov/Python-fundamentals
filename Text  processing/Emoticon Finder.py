text = input()
symbols = ''
for i in range(len(text)):

    if text[i] == ':':
        symbols += text[i] + text[i + 1] + '\n'
print(symbols)