lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

cost = 0
shield_breaks = 0
for day in range(1, lost_fights + 1):

    if day % 2 == 0:
        cost += helmet_price
    if day % 3 == 0:

        cost += sword_price
        if day % 3 == 0 and day % 2 == 0:
            cost += shield_price
            shield_breaks += 1
            if shield_breaks % 2 == 0:
                cost += armor_price

print(f"Gladiator expenses: {cost} aureus")
