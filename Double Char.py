text = input()

new_text = ''

for char in range(len(text)):
    new_text += text[char] * 2

print(new_text, end='')


