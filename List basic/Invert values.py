numbers = input().split(' ')

converted_numbers = []

for num in numbers:

    current_num = int(num)
    if current_num >= 0:

        converted_numbers.append(-current_num)
    else:
        converted_numbers.append(abs(current_num))

print(converted_numbers)

