def sum_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(subtract_numbers(sum_numbers(num1, num2), num3))
