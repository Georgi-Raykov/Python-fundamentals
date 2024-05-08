text = input()

indices = []

for i in range(len(text)):

    if 60 <= ord(text[i]) <= 90:
        indices.append(i)

print(indices)

