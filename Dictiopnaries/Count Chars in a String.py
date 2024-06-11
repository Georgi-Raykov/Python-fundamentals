text = input()

dict_counter = {}

for i in range(len(text)):

    if text[i] != ' ':

        if text[i] not in dict_counter:
            dict_counter[text[i]] = 0
        dict_counter[text[i]] += 1

for key, value in dict_counter.items():
    print(f"{key} -> {value}")
