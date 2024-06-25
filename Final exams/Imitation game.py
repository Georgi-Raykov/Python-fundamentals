
text = input()
command = input()


while command != 'Decode':

    lines = command.split('|')

    if lines[0] == 'Move':
        numbers = int(lines[1])

        piece_letter = text[0:numbers]
        text = text[numbers:] + piece_letter
    elif lines[0] == 'Insert':
        index = int(lines[1])
        value = lines[2]
        text = text[0:index] + value + text[index:]
    elif lines[0] == 'ChangeAll':
        substring = lines[1]
        replacement = lines[2]

        if substring in text:
            text = text.replace(substring, replacement)

    command = input()

print(f"Decrypted message is: {text}")