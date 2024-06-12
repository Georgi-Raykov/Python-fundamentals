
register = {}
while True:

    command = input().split(' : ')

    if command[0] == 'end':
        break

    course = command[0]
    name = command[1]

    if course not in register:

        register[course] = []
    register[course].append(name)

for key, value in register.items():

    print(f"{key}: {len(value)}")
    for val in value:
        print(f"--{val}")