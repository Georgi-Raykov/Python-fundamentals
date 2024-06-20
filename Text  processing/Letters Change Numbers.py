import string

items = input().split()
number_storage = []
total_sum = 0
for item in items:
    first_letter = item[0]
    number = int(item[1:-1])
    last_letter = item[-1]
    current_number = 0
    result = 0

    alphabet_index = string.ascii_lowercase
    index_first_letter = alphabet_index.index(first_letter.lower()) + 1
    index_last_letter = alphabet_index.index(last_letter.lower()) + 1

    if first_letter.isupper():

        current_number += number / index_first_letter
    elif first_letter.islower():
        current_number += number * index_first_letter
    if last_letter.isupper():
        result += current_number - index_last_letter
    elif last_letter.islower():
        result += current_number + index_last_letter
    number_storage.append(result)
    total_sum = sum(number_storage)

print(f"{total_sum:.2f}")
