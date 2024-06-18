def multiply_chars(first, second):
    total_result = 0
    for i in range(len(first)):

        if i < len(second):
            total_result += ord(first[i]) * ord(second[i])
        else:
            total_result += ord(first[i])
    return total_result


def base_logical(symbol):
    first_symbols = symbol[0]
    second_symbols = symbol[1]

    if len(first_symbols) > len(second_symbols):
        result = multiply_chars(first_symbols, second_symbols)
        return result
    else:
        result = multiply_chars(second_symbols, first_symbols)
        return result


symbols = input().split()
print(base_logical(symbols))