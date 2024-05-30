price_without_taxes = 0
taxes = 0
total_price = 0
price_with_taxes = 0

while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    part_price = float(command)
    if part_price < 0:
        print("Invalid price!")
    else:
        price_without_taxes += part_price

taxes = price_without_taxes * 0.20
price_with_taxes = price_without_taxes + taxes
if price_without_taxes == 0:
    print("Invalid order!")
else:

    if command == 'special':
        special_discount = price_with_taxes * 0.10
        total_price = price_with_taxes - special_discount
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
    elif command == 'regular':
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {price_with_taxes:.2f}$")
