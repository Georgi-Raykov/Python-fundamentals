def modifier_array(num):
    command = input()

    while command != 'end':
        data = command.split()

        type_command = data[0]

        if type_command == 'swap':

            index1 = int(data[1])
            index2 = int(data[2])

            num[index1], num[index2] = num[index2], num[index1]
        elif type_command == 'multiply':
            index1 = int(data[1])
            index2 = int(data[2])
            multip_num = num[index1] * num[index2]
            num[index1] = multip_num
        elif type_command == 'decrease':

            for i in range(len(num)):
                num[i] -= 1

        command = input()
    new_list = [str(x) for x in num]
    return ', '.join(new_list)


numbers = [int(x) for x in input().split()]
print(modifier_array(numbers))
