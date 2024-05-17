people = input().split()
k = int(input())

execution_order = []
index = 0
while len(people) > 0:
    index = (index + k - 1) % len(people)
    execution_order.append(people.pop(index))
print(execution_order)