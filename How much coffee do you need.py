command = input()
counter = 0
while command != 'END':
    events = command

    if events.lower() == 'cat' or events.lower() == 'dog' or events.lower() == 'coding' or events.lower() == 'movie':
        if events.isupper():
            counter += 2
        else:
            counter += 1

    command = input()
if counter > 5:
    print('You need extra sleep')
else:

  print(counter)
