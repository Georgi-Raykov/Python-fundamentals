def create_dictionary(items):
    store_items = {}
    for i in range(0, len(items), 2):

        key = items[i]
        value = items[i + 1]
        store_items[key] = value
    return store_items


foods = input().split()
print(create_dictionary(foods))