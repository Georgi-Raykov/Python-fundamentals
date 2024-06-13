n = int(input())
grade_dict = {}
for i in range(n):

    student = input()
    grade = float(input())

    if student not in grade_dict:
        grade_dict[student] = []

    grade_dict[student].append(grade)

for key, value in grade_dict.items():
    total_sum = sum(value)
    average = total_sum / len(value)
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")
