import re

text = input()

words = ['fish', 'water', 'sun', 'sand']
counter = 0
for word in words:
    counter += len(re.findall(word, text, re.IGNORECASE))

print(counter)
