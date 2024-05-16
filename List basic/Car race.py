numbers = input().split()

middle_index = len(numbers) // 2

left_car = numbers[:middle_index]
right_car = numbers[middle_index + 1:]
reversed_right_car = right_car[::-1]

left_scores = 0
right_scores = 0

for i in range(middle_index):

    if int(left_car[i]) == 0:
        left_scores = left_scores * 0.8
    else:
        left_scores += int(left_car[i])
    if int(right_car[i]) == 0:
        right_scores = right_scores * 0.8
    else:
        right_scores += int(right_car[i])

if right_scores < left_scores:
    print(f"The winner is right with total time: {right_scores:.1f}")
else:
    print(f"The winner is left with total time: {left_scores:.1f}")









