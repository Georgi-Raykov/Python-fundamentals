budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_eggs = price_per_kg_flour * 0.75

price_per_one_litters_milk = (price_per_kg_flour * 0.25) + price_per_kg_flour
price_milk_per_one_bread = price_per_one_litters_milk / 4

total_sum_per_one_bread = price_per_kg_flour + price_per_pack_eggs + price_milk_per_one_bread
current_count_bread = 0
colored_eggs = 0

while budget >= total_sum_per_one_bread:

    budget -= total_sum_per_one_bread
    colored_eggs += 3
    current_count_bread += 1
    if current_count_bread % 3 == 0:
        colored_eggs -= current_count_bread - 2

print(f"You made {current_count_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")











