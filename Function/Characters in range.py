def characters_range(a, b):
    chars = []
    for i in range(ord(a) + 1, ord(b)):
        chars.append(chr(i))
    return chars


first = input()
second = input()
print(' '.join(characters_range(first, second)))
