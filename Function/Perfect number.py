def perfect_number(num):
    divisors_numbers = []
    for i in range(1, num):

        if num % i == 0:
            divisors_numbers.append(i)
    if sum(divisors_numbers) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number(number)
