number = int(input())

wagons = [0 for i in range(number)]

command = input()

while command != 'End':

    line_commands = command.split()

    first_part_command = line_commands[0]

    if first_part_command == 'add':

        wagons[-1] += int(line_commands[1])
    elif first_part_command == 'insert':
        index = int(line_commands[1])
        num = int(line_commands[2])
        wagons[index] += num
    elif first_part_command == 'leave':
        index = int(line_commands[1])
        num = int(line_commands[2])
        wagons[index] -= num

    command = input()

print(wagons)
