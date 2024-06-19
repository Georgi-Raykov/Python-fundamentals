explosion_string = input()

rest_of_explosion = 0
rest_explosion = False
for i in range(len(explosion_string)):
    index = i + 1
    if 0 <= index < len(explosion_string):
        if explosion_string[i] == '>' and explosion_string[i + 1].isdigit():

            explosion = int(int(explosion_string[i + 1]))
            if int(explosion_string[i + 1]) >= 2:
                if explosion_string[i + 2] == '>':
                    rest_of_explosion += int(explosion_string[i + 1]) - 1
                    rest_explosion = True
                    explosion_string = explosion_string[0:index] + explosion_string[index + 1:]
                elif explosion_string[i + 2] != '>':
                    if rest_explosion:
                        explosion = int(int(explosion_string[i + 1])) + rest_explosion
                        explosion_string = explosion_string[0:index] + explosion_string[index + explosion:]
                        rest_explosion = False
                        rest_of_explosion = 0
                    else:
                        explosion_string = explosion_string[0:index] + explosion_string[index + explosion:]
            else:
                if explosion_string[i + 2] != '>' and rest_explosion:
                    explosion = int(int(explosion_string[i + 1])) + rest_of_explosion
                    explosion_string = explosion_string[0:index] + explosion_string[index + explosion:]
                    rest_explosion = False
                    rest_of_explosion = 0
                else:
                    explosion_string = explosion_string[0:index] + explosion_string[index + 1:]

print(explosion_string)