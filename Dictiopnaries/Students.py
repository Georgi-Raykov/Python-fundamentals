data = input()
base_data = {}
while ':' in data:
    info = data.split(':')

    name = info[0]
    id_number = info[1]
    program = info[2]

    if program not in base_data:
        base_data[program] = {}

    base_data[program][id_number] = name

    data = input()

data = data.replace('_', ' ')


for id in base_data[data]:

    print(f"{base_data[data][id]} - {id}")


