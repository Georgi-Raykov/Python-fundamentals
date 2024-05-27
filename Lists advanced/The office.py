employees = input().split()
factor = int(input())

after_mapping = list(map(lambda x: int(x) * factor, employees))

happy_employees = list(filter(lambda x: x >= (sum(after_mapping) / len(employees)), after_mapping))

if len(happy_employees) >= len(employees) / 2:

    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")

else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
