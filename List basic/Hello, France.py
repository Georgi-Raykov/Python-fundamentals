products = input().split('|')

budget = int(input())

new_prices = []
profit = 0

is_valid = False

for i in range(len(products)):

    is_valid = False
    current_product = products[i]

    type_product = current_product.split('->')
    price = float(type_product[1])
    product = type_product[0]

    if product == 'Clothes' and price <= 50.00:
        is_valid = True
    elif product == 'Shoes' and price <= 35.00:

        is_valid = True
    elif product == 'Accessories' and price <= 20.50:

        is_valid = True

    if is_valid and budget >= price:
        budget -= price
        profit += price * 0.40
        new_price = price + (price * 0.40)
        new_price = f"{new_price:.2f}"
        new_prices.append(new_price)

sum_new_prices = sum(map(float, new_prices))

print(' '.join(map(str, new_prices)))
print(f"Profit: {profit:.2f}")

if budget + sum_new_prices >= 150:
    print("Hello France!")
