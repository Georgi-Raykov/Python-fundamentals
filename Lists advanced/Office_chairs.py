def office_chairs(num):
    free_chairs = 0
    condition = 0
    for room in range(1, num + 1):
        lines = input().split()
        chairs = lines[0]
        people = int(lines[1])

        diff = abs(len(chairs) - people)

        if len(chairs) >= people:
            free_chairs += diff
            condition += 1
        else:
            print(f"{diff} more chairs needed in room {room}")
    if condition == num:
        print(f"Game On, {free_chairs} free chairs left")


number = int(input())

office_chairs(number)