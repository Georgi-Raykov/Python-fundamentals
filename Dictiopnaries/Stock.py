def stocks(items, searching):
    stock_dict = {}

    for i in range(0,len(items), 2):
        stock = items[i]
        quantity = items[i + 1]

        stock_dict[stock] = quantity

    for word in searching:
        if word in stock_dict:
            print(f"We have {stock_dict[word]} of {word} left")
        else:
            print(f"Sorry, we don't have {word}")


items_stocks = input().split()
searching_stocks = input().split()

stocks(items_stocks, searching_stocks)