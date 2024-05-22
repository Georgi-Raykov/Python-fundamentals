def factorial_number(num1, num2):
    result = 0
    fact = 1
    for i in range(1, num1 + 1):
        fact = fact * i
    result = fact / num2

    return result


number1 = int(input())
number2 = int(input())

print(factorial_number(number1, number2))
