text = input()
current_ch = ''
correct_string = ''
for i in range(len(text)):

    if text[i] != current_ch:
        correct_string += text[i]
        current_ch = text[i]
    else:
        continue

print(correct_string)