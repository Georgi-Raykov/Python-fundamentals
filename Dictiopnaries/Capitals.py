countries = input().split(', ')
capitals = input().split(', ')

result = zip(countries, capitals)

for key, value in result:
    print(f"{key} - > {value}")
