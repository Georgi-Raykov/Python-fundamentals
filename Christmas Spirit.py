quantity = int(input())
days = int(input())
spirit = 0
total = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total += 2 * quantity
        spirit += 5
    if day % 3 == 0:
        total += 5 * quantity + 3 * quantity
        spirit += 13

    if day % 5 == 0:

        total += 15 * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:

        spirit -= 20
        total += 23
        if day == days:
            spirit -= 30

print(f"{total}")
print(f"{spirit}")
