number = int(input())

for n in range(1, number + 1):

    working_number = n
    sum_digits = 0

    while working_number > 0:
        sum_digits += working_number % 10
        working_number = int(working_number / 10)

    is_special = sum_digits == 5 or sum_digits == 7 or sum_digits == 11

    print(f"{n} -> {is_special}")

