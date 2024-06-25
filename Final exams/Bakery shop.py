command = input()
information = {}

sale_products = 0
while command != 'Complete':
    data = command.split()

    if data[0] == 'Receive':
        quantity = int(data[1])
        food = data[2]
        if quantity > 0:

            if food not in information:
                information[food] = 0
            information[food] += quantity
    elif data[0] == 'Sell':
        quantity = int(data[1])
        food = data[2]

        if food not in information:
            print(f"You don't have any {food}")
        elif quantity > information[food]:
            sale_products += information[food]
            print(f"There aren't enough {food}. You sold the last {information[food]} of them.")
            information[food] = 0
            information.pop(food)


        else:

            information[food] -= quantity
            sale_products += quantity
            print(f"You sold {quantity} {food}.")
            if information[food] == 0:
                information.pop(food)

    command = input()
for key, value in information.items():

    print(f"{key}: {value}")

print(f"All sold: {sale_products} goods.")