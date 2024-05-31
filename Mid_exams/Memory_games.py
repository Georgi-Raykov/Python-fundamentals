def memory_game(string):
    command = input()
    movies = 0
    is_finish = False
    while command != 'end':
        indices = command.split()
        idx1 = int(indices[0])
        idx2 = int(indices[1])

        if 0 <= idx1 < len(string) and 0 <= idx2 < len(string):

            if string[idx1] == string[idx2]:
                print(f"Congrats! You have found matching elements - {string[idx1]}")
                for i in string:
                    if i == string[idx1]:
                        while i in string:
                            string.remove(i)
                        break

                movies += 1
            else:
                print("Try again")

        else:
            if len(string) > 0:
                print("Invalid input! Adding additional elements to the board")
                index = len(string) // 2
                add_element = ''
                for i in range(len(string) - 1):
                    if string[i] == string[i + 1]:
                        add_element = 'a' + string[i]
                        break
                string.insert(index, add_element)
                string.insert(index + 1, add_element)
            else:
                is_finish = True
                print(f'You have won in {movies} turns!')

        command = input()
        if command == 'end' and not is_finish:
            if len(string) > 0:
                print('Sorry you lose :(')
                print(' '.join(string))
            else:
                print(f'You have won in {movies} turns!')


elements = input().split()
memory_game(elements)
