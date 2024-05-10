number = int(input())

brackets = []
is_balanced = False
for i in range(number):

    symbol = input()

    if symbol == '(' or symbol == ')':
        brackets.append(symbol)
for j in range(0, len(brackets) - 1):

    if brackets[j] != brackets[j + 1]:
        if len(brackets) % 2 == 0:
            is_balanced = True

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
