word = input()

vowels = ['a', 'o', 'u', 'e', 'i']

new_word = [word[i] for i in range(len(word)) if word[i].lower() not in vowels]

str_new_word = ''.join(new_word)

print(str_new_word)

