events = input().split('|')

energy = 100
coins = 100

counter = 0

for i in range(len(events)):

    event = events[i].split('-')

    type_event = event[0]
    count = int(event[1])

    if type_event == 'rest':

        if energy + count > 100:
            gained_energy = 100 - energy
            energy += gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:

            energy += count
            print(f"You gained {count} energy.")
            print(f"Current energy: {energy}.")
    elif type_event == 'order':

        if energy - 30 <= 0:
            energy += 50
            print("You had to rest!")
        else:

            coins += count
            energy -= 30
            print(f"You earned {count} coins.")
    else:

        if coins >= count:

            coins -= count
            print(f"You bought {type_event}.")
        else:

            print(f"Closed! Cannot afford {type_event}.")
            break

    counter += 1

if counter == len(events):
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




