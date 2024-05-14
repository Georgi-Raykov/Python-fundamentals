n = int(input())

word= input()

search_text = []
words = []
for i in range(n):

    text = input()
    search_text.append(text)

for searching in search_text:

    if word in searching:
        words.append(searching)

print(search_text)
print(words)
