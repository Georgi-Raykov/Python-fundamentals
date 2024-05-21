numbers = input().split()
even_numbers = list(filter(lambda a: a % 2 == 0, map(int, numbers)))

print(even_numbers)






