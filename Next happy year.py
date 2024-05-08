year = int(input())
is_happy = False
while not is_happy:
    year += 1
    str_year = str(year)
    set_year = set(str_year)
    is_happy = len(set_year) == len(str_year)

print(year)


