first_string = input()
second_string = input()

for i in range(len(first_string)):

    if first_string[i] != second_string[i]:

        new_part = second_string[i]

        word = first_string[0:i] + new_part + first_string[i + 1:]
        first_string = word
        print(first_string)

