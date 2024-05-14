key = int(input())

n = int(input())
message = ''
for _ in range(n):
    ch = input()
    num_ch = ord(ch) + key
    new_ch = chr(num_ch)
    message += new_ch

print(message)