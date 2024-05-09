start = int(input())
end = int(input())

result = ''
for ch in range(start, end + 1):

    result += chr(ch)

print(result, end=' ')