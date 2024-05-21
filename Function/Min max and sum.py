list_numbers = input().split()

numbers = list(map(int, list_numbers))

print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")