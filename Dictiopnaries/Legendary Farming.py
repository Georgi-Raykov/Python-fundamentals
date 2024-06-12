def item_solve(item_dict, mat, quant):
    item_dict[mat] += quant

    return item_dict


def junk_solve(junk, mat, quant):
    if mat not in junk:
        junk[mat] = 0
    junk[mat] += quant

    return junk


materials = input().split()
junks = {}
items = {'shards': 0, 'fragments': 0, 'motes': 0}
key_materials = ['shards', 'fragments', 'motes']
condition = None
winner = ''
for i in range(0, len(materials), 2):
    quantity = int(materials[i])
    material = materials[i + 1]
    if material.lower() not in key_materials:
        condition = junk_solve(junks, material, quantity)
    else:
        condition = item_solve(items, material.lower(), quantity)
    if material.lower() in items:
        if items[material.lower()] >= 250:
            if items[material.lower()] > 250:
                items[material.lower()] = items[material.lower()] - 250
                winner = material.lower()
            break

if winner == 'shards':
    print("Shadowmourne obtained!")
elif winner == 'fragments':
    print("Valanyr obtained!")
elif winner == 'motes':
    print("Dragonwrath obtained!")

for key, value in items.items():
    print(f"{key}: {value}")
for key, value in junks.items():
    print(f"{key}: {value}")
