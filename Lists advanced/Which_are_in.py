def find_substring(sub, word):
    result = []
    for s in sub:
        if s in words:
            result.append(s)
    return result


substrings = input().split(', ')
words = input()

print(find_substring(substrings, words))
