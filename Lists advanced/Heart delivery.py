def heart_solve(houses):
    command = input()
    valentin_days = 0
    current_index = 0
    while command != 'Love!':
        is_boolean = False
        data_line = command.split()

        index = int(data_line[1])

        current_index += index
        if current_index >= len(houses):
            current_index = 0
            is_boolean = True
        else:
            is_boolean = True
        if is_boolean:

            if houses[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")
            elif houses[current_index] - 2 == 0:
                valentin_days += 1
                houses[current_index] -= 2
                print(f"Place {current_index} has Valentine's day.")
            else:

                houses[current_index] -= 2

        command = input()
    print(f"Cupid's last position was {current_index}.")
    if valentin_days == len(houses):
        print("Mission was successful.")
    else:
        result = len(houses) - valentin_days
        print(f"Cupid has failed {result} places.")


row = [int(x) for x in input().split('@')]
heart_solve(row)
