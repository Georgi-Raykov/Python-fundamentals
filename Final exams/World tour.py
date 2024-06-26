text = input()
command = input()

while command != 'Travel':

    line = command.split(':')
    if line[0] == 'Add Stop':
        index = int(line[1])
        string = line[2]
        if 0 <= index < len(text):
            text = text[0:index] + string + text[index:]
            print(text)
    elif line[0] == 'Remove Stop':
        start = int(line[1])
        end = int(line[2])

        if 0 <= start < len(text) and 0 <= end < len(text):
            text = text[0:start] + text[end + 1:]
            print(text)
    elif line[0] == 'Switch':
        old_string = line[1]
        new_string = line[2]

        if old_string in text:

            text = text.replace(old_string, new_string)
            print(text)

    command = input()
print(f"Ready for world tour! Planned stops: {text}")