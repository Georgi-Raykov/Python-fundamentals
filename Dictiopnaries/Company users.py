
register = {}
while True:

    data = input().split(' -> ')

    if data[0] == 'End':
        break

    company_name = data[0]
    id_number = data[1]

    if company_name not in register:

        register[company_name] = set()
    register[company_name].add(id_number)

for key, value in register.items():
    print(f"{key}")
    for id in value:
        print(f"--{id}")