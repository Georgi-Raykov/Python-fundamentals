n = int(input())
base_data = {}
for i in range(n):

    command = input().split()
    type = command[0]

    if type == 'register':
        name = command[1]
        number = command[2]

        if type not in base_data:
            base_data[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {base_data[name]}")
    elif type == 'unregister':
        name = command[1]

        if name not in base_data:
            print(f"ERROR: user {name} not found")
        else:
            del base_data[name]
            print(f"{name} unregistered successfully")

for key, value in base_data.items():
    print(f"{key} => {value}")
