def odd_and_even_sum(num):
    odd = []
    even = []
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even.append(int(num[i]))
        else:
            odd.append(int(num[i]))
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


number = input()
print(odd_and_even_sum(number))
