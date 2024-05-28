def electron_distribution(num):
    shells = []
    electrons = num
    for i in range(1, 10 + 1):

        formula = 2 * (i ** 2)

        if electrons - formula > 0:
            electrons -= formula
            shells.append(formula)
        else:
            shells.append(electrons)

            break
    return shells


number = int(input())

print(electron_distribution(number))

