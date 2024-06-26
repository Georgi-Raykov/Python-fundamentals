n = int(input())

information = {}

for i in range(n):

    data = input().split('<->')
    plant = data[0]
    rarity = int(data[1])

    if plant not in information:
        information[plant] = {'rarity': rarity, 'rating': []}

command = input()

while command != 'Exhibition':

    line = command.split(': ')

    if line[0] == 'Rate':

        command_part = line[1].split(' - ')
        plant = command_part[0]
        rate = float(command_part[1])
        information[plant]['rating'].append(rate)
    elif line[0] == 'Update':

        command_part = line[1].split(' - ')
        plant = command_part[0]
        rate = int(command_part[1])

        information[plant]['rarity'] = rate
    elif line[0] == 'Reset':

        plant = line[1]

        information[plant]['rating'].clear()

    command = input()
print("Plant for exhibition:")

for key, value in information.items():
    if len(value['rating']) > 0:
        rating = sum(value['rating']) / len(value['rating'])
    else:
        rating = 0

    print(f"{key}; Rarity: {value['rarity']}; Rating: {rating:.2f}")
