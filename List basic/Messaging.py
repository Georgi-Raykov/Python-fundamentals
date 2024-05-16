numbers = input().split()
text = input()

message = ''

for number in numbers:
    index = 0
    char = ''
    for i in range(len(number)):
        index += int(number[i])
    if index > len(text):
        char = text[index % len(text)]
        index = index % len(text)
    else:
        char = text[index]
    message += char
    new_text = text[:index] + text[index + 1:]
    text = new_text
print(message)