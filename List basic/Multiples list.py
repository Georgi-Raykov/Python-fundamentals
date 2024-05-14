factor = int(input())
count = int(input())

numbers = []

for num in range(1, count + 1):
    numbers.append(factor * num)

print(numbers)