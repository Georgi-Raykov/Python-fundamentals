gifts = input().split()

command = input()

while command != 'No Money':
    current_command = command.split()

    if current_command[0] == 'OutOfStock':
        if current_command[1] in gifts:
            for i in range(len(gifts)):
                if gifts[i] == current_command[1]:
                    gifts[i] = 'None'
    elif current_command[0] == 'Required':
        index = int(current_command[2])
        gift = current_command[1]
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif current_command[0] == 'JustInCase':
        gifts[-1] = current_command[1]

    command = input()

print(' '.join([gift for gift in gifts if gift != 'None']))
