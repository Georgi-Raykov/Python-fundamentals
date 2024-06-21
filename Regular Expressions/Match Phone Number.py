import re

text = input()
regex = r"\+359([ -])2\1\d{3}\1\d{4}\b"

matches = re.finditer(regex, text)

for match in matches:
    print(match.group())
