def palindrome(num):

    for n in num:
        if n == n[::-1]:
            print('True')
        else:
            print('False')


numbers = input().split(', ')
palindrome(numbers)



