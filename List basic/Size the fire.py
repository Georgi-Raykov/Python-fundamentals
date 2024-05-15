fires = input().split('#')
water = int(input())

efforts = 0
fire_cells = []
is_valid = False
for i in range(len(fires)):

    fire = fires[i]
    type_of_fire = fire.split(' = ')
    fire_power = int(type_of_fire[1])

    if water >= fire_power:

        if type_of_fire[0] == 'High' and 81 <= fire_power <= 125:

            is_valid = True

        elif type_of_fire[0] == 'Medium' and 51 <= fire_power <= 80:

            is_valid = True

        elif type_of_fire[0] == 'Low' and 1 <= fire_power <= 50:

            is_valid = True
        if is_valid:
            water -= fire_power
            efforts += fire_power * 0.25
            fire_cells.append(fire_power)
print('Cells:')

for i in fire_cells:
    print(f"- {i}")
print(f"Effort: {efforts:.2f}")
print(f"Total fire: {sum(fire_cells)}")
