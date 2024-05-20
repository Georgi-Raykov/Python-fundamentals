numbers = input().split()

new_numbers = []

for n in numbers:

    new_numbers.append(abs(float(n)))

print(new_numbers)