n = int(input())
dict_synonyms = {}
for i in range(n):

    key = input()
    synonym = input()

    if key not in dict_synonyms:

        dict_synonyms[key] = []

    dict_synonyms[key].append(synonym)

for key, value in dict_synonyms.items():

    print(f"{key} - {', '.join(value)}")

