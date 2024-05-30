people = int(input())
wagons = [int(x) for x in input().split()]

max_capacity = len(wagons) * 4

for i in range(len(wagons)):

    persons_per_wagon = 4

    if people - persons_per_wagon <= 0:
        add = persons_per_wagon - (abs(people - persons_per_wagon))
        wagons[i] += add
        people -= add
        result = list(map(lambda x: str(x), wagons))
        print(f"The lift has empty spots!")
        print(' '.join(result))
        break
    people -= persons_per_wagon

    if wagons[i] == 0:
        wagons[i] += persons_per_wagon
    else:
        add = abs(wagons[i] - persons_per_wagon)
        wagons[i] += add
        people += add
    if sum(wagons) >= max_capacity:
        add = max_capacity - sum(wagons)
        if people >= add:
            wagons[i] += add
            people -= add
        print(f"There isn't enough space! {people} in a queue!")
        break
