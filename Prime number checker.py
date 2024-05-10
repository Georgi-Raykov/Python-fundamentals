import math

number = int(input())

square_root = int(math.sqrt(number))
is_prime = False
for n in range(2, square_root + 1):

    if number % n != 0:
        is_prime = True
    else:
        is_prime = False
        break

print(is_prime)
