def craft(items):
    command = input()
    while command != 'Craft!':

        data = command.split(' - ')
        type_command = data[0]

        if type_command == 'Collect':
            item = data[1]

            if item not in items:
                items.append(item)
        elif type_command == 'Drop':

            item = data[1]
            if item in items:
                items.remove(item)
        elif type_command == 'Combine Items':
            second_command_part = data[1].split(':')
            old_item = second_command_part[0]
            new_item = second_command_part[1]

            if old_item in items:
                for i, value in enumerate(items):
                    if value == old_item:
                        items.insert(i + 1, new_item)
        elif type_command == 'Renew':

            item = data[1]
            if item in items:
                items.remove(item)
                items.append(item)

        command = input()
    return ', '.join(items)


craft_items = input().split(', ')
print(craft(craft_items))
