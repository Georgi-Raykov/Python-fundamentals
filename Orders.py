orders = int(input())

total = 0

for order in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    orders_price = days * capsules_count * price_per_capsule

    total += orders_price

    print(f"The price for the coffee is: ${orders_price:.2f}")

print(f"Total: ${total:.2f}")
