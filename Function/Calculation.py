def Calculation(num1, num2, operator):
    if operator == "add":

        return num1 + num2
    elif operator == 'subtract':

        return num1 - num2
    elif operator == 'multiply':

        return num1 * num2
    elif operator == 'divide':

        return int(num1 / num2)


op = input()
number1 = int(input())
number2 = int(input())

print(Calculation(number1, number2, op))
