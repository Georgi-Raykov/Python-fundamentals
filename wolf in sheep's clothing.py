animals = input()

list_animals = animals.split(', ')
list_animals.reverse()

wolf = 0

for index in range(len(list_animals)):

    if list_animals[index] == 'wolf':
        wolf = index
        if wolf - 1 < 0:
            print("Please go away and stop eating my sheep")
        else:
            wolf -= 1
            print(f"Oi! Sheep number {wolf + 1}! You are about to be eaten by a wolf!")
        break
