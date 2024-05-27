command = input()

notes = ['' for i in range(11)]
while command != 'End':
    line = command.split('-')

    index = int(line[0])
    item = line[1]

    notes.insert(index, item)

    command = input()
new_notes = [i for i in notes if i != '']
print(new_notes)