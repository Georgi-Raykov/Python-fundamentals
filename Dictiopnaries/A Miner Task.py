miner_dict = {}

while True:

    command = input()

    if command == 'stop':
        break

    quantity = int(input())
    if command not in miner_dict:
        miner_dict[command] = quantity

    else:
        miner_dict[command] += quantity

for key, value in miner_dict.items():
    print(f"{key} -> {value}")

