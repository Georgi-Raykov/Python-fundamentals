statistic = {}
submissions = {}

command = input()

while command != 'exam finished':
    data = command.split('-')

    if 'banned' not in data:
        name = data[0]
        language = data[1]
        points = int(data[2])
        if name not in statistic:
            statistic[name] = points

        else:
            if statistic[name] < points:
                statistic[name] = points
        if language not in submissions:

            submissions[language] = 0
        submissions[language] += 1
    else:
        name = data[0]
        statistic.pop(name)

    command = input()

print("Results:")
for key, value in statistic.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")