numbers = [int(x) for x in input().split(', ')]

positive = [str(i) for i in numbers if i >= 0]
negative = [str(i) for i in numbers if i < 0]
even = [str(i) for i in numbers if i % 2 == 0]
odd = [str(i) for i in numbers if i % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
