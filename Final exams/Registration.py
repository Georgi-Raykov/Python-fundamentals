name = input()

command = input()

while command != 'Registration':

    line = command.split(' ')

    if line[0] == 'Letters':
        if line[1] == 'Lower':
            current = name.lower()
            print(f"{current}")
        elif line[1] == 'Upper':
            current = name.upper()
            print(f"{current}")
    elif line[0] == 'Reverse':
        start = int(line[1])
        end = int(line[2])
        if 0 <= start < len(name) and 0 <= end < len(name):

            current = name[start:end + 1]
            current = current[::-1]
            print(f"{current}")
    elif line[0] == 'Substring':

        substring = line[1]

        if substring in name:

            name = name.replace(substring, '')
            print(f"{name}")
        else:
            print(f"The username {name} doesn't contain {substring}")

    elif line[0] == 'Replace':

        ch = line[1]
        if ch in name:

            name = name.replace(ch, '-')
            print(f"{name}")

    elif line[0] == 'IsValid':
        ch = line[1]

        if ch in name:
            print("Valid username")
        else:
            print(f"{ch} must be contained in your username.")








    command = input()