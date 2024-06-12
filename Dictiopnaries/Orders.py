
orders = {}


while True:

    command = input().split()

    if command[0] == 'buy':
        break

    name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if name not in orders:
        orders[name] = {'price': price, 'quantity': quantity}
    else:
        orders[name]['price'] = price
        orders[name]['quantity'] += quantity

for key, value in orders.items():

    result = value['price'] * value['quantity']
    print(f"{key} -> {result:.2f}")




