items = input()

new_items = ''
i = 0
while len(items) > 0:

    if items[i].isdigit():
        number = int(items[i])
        index = i

        new_items += items[0:index].upper() * number
        items = items[index + 1:]
        index = 0
        i = 0
    else:
      i += 1
print(new_items)