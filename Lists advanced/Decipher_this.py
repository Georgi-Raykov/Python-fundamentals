def decipher(message):
    new_message = []

    for word in message:
        str_number = ''
        number = 0
        for i in word:
            if i.isdigit():
                str_number += i
        number = int(str_number)
        ch = chr(number)
        word = word.replace(str_number, '')
        word = word[::-1]
        word = ch + word
        new_message.append(word)
    return ' '.join(new_message)


words = input().split()
print(decipher(words))
