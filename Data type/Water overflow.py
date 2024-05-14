number = int(input())
tank = 0
for _ in range(0, number):

    water = int(input())

    if tank + water <= 255:

        tank += water
    else:
        print('Insufficient capacity')

print(f"{tank}")

