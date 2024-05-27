strings = input().split()
palindrome = input()
count = 0
all_palindromes = [word for word in strings if word == word[::-1]]

count += all_palindromes.count(palindrome)

print(all_palindromes)
print(f"Found palindrome {count} times")