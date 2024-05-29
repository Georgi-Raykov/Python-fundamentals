numbers = input().split()

command = input()

while command != 'end':
    line_command = command.split()

    type_command = line_command[0]

    if type_command == 'exchange':
        index = int(line_command[1])
        if 0 <= index < len(numbers):
           new_numbers = numbers[index + 1:] + numbers[:index + 1]
        else:
            print("Invalid index")
    elif type_command == 'max':
        ...






    command = input()
