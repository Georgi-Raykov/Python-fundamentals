def orders(product, quantity):
    result = 0
    if product == 'coffee':

        result = quantity * 1.50
    elif product == 'water':

        result = quantity * 1.00
    elif product == 'coke':
        result = quantity * 1.40
    elif product == 'snacks':
        result = quantity * 2.00
    return f"{result:.2f}"


type_drink = input()
type_quantity = int(input())

print(orders(type_drink, type_quantity))
