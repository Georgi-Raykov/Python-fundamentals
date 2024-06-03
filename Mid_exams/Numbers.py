def greater_from_avg(num):
    data_list = []
    average_number = sum(num) / len(num)

    if len(num) == 1:
        return 'No'

    for n in numbers:
        if n > average_number:
            data_list.append(n)

    data_list = sorted(data_list, key=lambda x: -x)
    if len(data_list) > 5:
        del data_list[5:]
    convert_to_string = list(map(lambda x: str(x), data_list))
    str_data = ' '.join(convert_to_string)

    return str_data


numbers = [int(x) for x in input().split()]
print(greater_from_avg(numbers))
