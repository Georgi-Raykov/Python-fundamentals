def solve(first, second, third, st):
    students_per_hour = first + second + third

    hours = 0
    while True:

        if st == 0:
            break
        hours += 1
        if hours % 4 != 0:

            if not st < students_per_hour:
                st -= students_per_hour

            else:
                st1 = st
                st -= st1

    return f"Time needed: {hours}h."


first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())
print(solve(first_employee, second_employee, third_employee, students))
