def loading_bar(number):
    number_percents = number // 10
    count_procents = '%' * number_percents
    count_points = '.' * (10 - number_percents)
    if number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"

    return f"{number}% [{count_procents}{count_points}]\nStill loading..."


n = int(input())
print(loading_bar(n))
