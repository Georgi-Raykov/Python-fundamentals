numbers = input().split(', ')


for i in range(len(numbers)):
    if numbers[i] == '0':
        numbers.append('0')
        numbers.remove(numbers[i])
print(numbers)