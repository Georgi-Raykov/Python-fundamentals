def CheckInfo(dict_book, number, finish):
    for i in range(number):

        name = input()
        if name in dict_book:
            print(f"{name} -> {dict_book[name]}")
        else:
            print(f"Contact {name} does not exist.")

        finish = True
    return finish


phoneBook = {}
is_finish = False
while True:

    info = input().split('-')
    condition = None
    if info[0].isdigit():
        condition = CheckInfo(phoneBook, int(info[0]), is_finish)
    if condition:
        break

    if info[0] not in phoneBook:

        phoneBook[info[0]] = info[1]
    else:
        phoneBook[info[0]] = info[1]
