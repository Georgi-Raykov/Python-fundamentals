words = {}
while True:

    word = input()
    if word == 'end':
        break

    reversed_word = ''.join(reversed(word))
    if word not in words:
        words[word] = reversed_word

for key, value in words.items():
    print(f"{key} = {value}")


