numbers = input().split()

n = int(input())

for _ in range(n):
    new_numbers = list(map(int, numbers))
    new_numbers.remove(min(new_numbers))
    numbers = new_numbers

print(', '.join(map(str, numbers)))