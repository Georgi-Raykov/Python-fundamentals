n = int(input())

collection = {}

for i in range(n):

    data = input().split('|')

    piece = data[0]
    composer = data[1]
    key = data[2]

    if piece not in collection:
        collection[piece] = {'composer': composer, 'key': key}

command = input()

while command != 'Stop':
    line = command.split('|')

    if line[0] == 'Add':
        piece = line[1]
        composer = line[2]
        key = line[3]
        if piece not in collection:
            collection[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif line[0] == 'Remove':
        piece = line[1]
        if piece in collection:

            collection.pop(piece)
            print(f"Successfully removed {piece}!")
        else:

            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif line[0] == 'ChangeKey':
        piece = line[1]
        new_key = line[2]
        if piece in collection:
            collection[piece]['key'] = new_key
            print(f"Changed the key of {piece} to new {new_key}")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()


for key, value in collection.items():

    print(f"{key} - > Composer: {value['composer']}, Key: {value['key']}")
