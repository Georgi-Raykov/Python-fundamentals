number = int(input())

for n in range(1, number + 1):

    working_number = n
    sum_digit = 0

    while working_number > 0:

        sum_digit += working_number % 10
        working_number = int(working_number / 10)

    special_number = sum_digit == 5 or sum_digit == 7 or sum_digit == 11

    print(n)