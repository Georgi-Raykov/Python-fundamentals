import re

text = input()

regex = r"([=/])[A-Z][A-Za-z]{3,}\1"

matches = re.finditer(regex, text)
destination = []
for match in matches:
    destination.append(match.group())

final_destinations = [x[1:-1] for x in destination]
travel_points = 0
for count in final_destinations:
    travel_points += len(count)
print(f"Destinations: {', '.join(final_destinations)}")
print(f"Travel points: {travel_points}")
