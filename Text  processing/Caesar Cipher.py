text = input()
crypt = ''
for ch in text:
    crypt += chr(ord(ch) + 3)

print(crypt)
