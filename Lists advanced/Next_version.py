def next_version(ver):
    number_version = int(''.join(ver)) + 1
    convert_to_string = [x for x in str(number_version)]
    final_result = '.'.join(convert_to_string)
    return final_result


version = input().split('.')
print(next_version(version))
