numbers = input().split(', ')
new_numbers = list(map(int, numbers))
even_numbers = [i for i in range(len(new_numbers)) if new_numbers[i] % 2 == 0]

print(even_numbers)