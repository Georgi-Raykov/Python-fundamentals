command = input()
force_side = {}

while command != 'Lumpawaroo':

    if '|' in command:
        data = command.split(' | ')
        side = data[0]
        name = data[1]
        exist_user = any(name in user for user in force_side.values())
        if not exist_user:
            if side not in force_side:
                force_side[side] = set()
            force_side[side].add(name)

    elif '->' in command:
        data = command.split(' -> ')
        name = data[0]
        side = data[1]
        exist_user = any(name in user for user in force_side.values())
        if not exist_user:
            force_side[side].add(name)
            print(f"{name} joins the {side} side!")
        else:
            for key, value in force_side.items():

                if name in value:
                    value.remove(name)
                    force_side[side].add(name)
                    print(f"{name} joins the {side} side!")

    command = input()
for key, value in force_side.items():
    count = len(value)
    if count > 0:
        print(f"Side: {key}, Members: {count}")
        for name in value:
            print(f"! {name}")
