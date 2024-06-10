command = input()
items = {}
while command != "statistics":
    data = command.split(': ')

    product = data[0]
    quantity = int(data[1])

    if product not in items:
        items[product] = quantity
    else:
        items[product] += quantity

    command = input()
print("Products in stock:")

for key, value in items.items():
    print(f"-{key}: {value}")
print(f"Total products: {len(items.keys())}")
print(f"Total Quantity: {sum(items.values())}")
