import re

text = input()

regex = r"([#\|])(?P<product>[A-Z][A-Za-z]+)\1(?P<date>[0-9]+/\d{2}/\d{2})\1(?P<calories>\d+)\1"

information = {}

matches = re.finditer(regex, text)
total_calories = 0
for match in matches:

    item = match.group('product')
    date = match.group('date')
    calories = match.group('calories')

    if item not in information:
        information[item] = []
    information[item].append(date)
    information[item].append(calories)

    total_calories += int(match.group('calories'))

days = total_calories // 2000

print(f"You have food to last you for {days} days!")

for key, value in information.items():
    print(f"Item: {key}, Best before: {value[0]}, Nutrition: {value[1]}")
