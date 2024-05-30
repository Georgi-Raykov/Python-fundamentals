def shoot_target(targets):
    command = input()
    while command != 'End':

        line = command.split()
        type_command = line[0]
        if type_command == 'Shoot':
            index = int(line[1])
            power = int(line[2])
            if 0 <= index < len(targets):
                targets[index] -= power
                if targets[index] <= 0:
                    targets.pop(index)
        elif type_command == 'Add':
            index = int(line[1])
            value = int(line[2])
            if 0 <= index < len(targets):
                targets.insert(index, value)
            else:
                print("Invalid placement!")
        elif type_command == 'Strike':

            index = int(line[1])
            radius = int(line[2])
            left_side = index - radius
            right_side = index + radius
            if 0 <= index < len(targets) and 0 <= left_side < len(targets) and 0 <= right_side < len(targets):
                del[targets[left_side:right_side + 1]]
            else:
                print("Strike missed!")

        command = input()
    result = [str(x) for x in targets]
    return '|'.join(result)


target_numbers = [int(x) for x in input().split()]
print(shoot_target(target_numbers))
