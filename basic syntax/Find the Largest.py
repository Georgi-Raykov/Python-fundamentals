number = input()

list_numbers = []

for i in range(len(number)):
    list_numbers.append(number[i])

list_numbers.sort(reverse=True)
print(''.join(list_numbers))
