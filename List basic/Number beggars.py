numbers = input().split(', ')
beggars = int(input())

home = [0] * beggars

for i in range(len(numbers)):

    home[i % beggars] += int(numbers[i])

print(home)
