def data_types(txt, number):
    result = 0
    text_result = ''
    if txt == 'int':
        result = int(number) * 2
        print(result)
    elif txt == 'real':

        result = int(number) * 1.5
        print(f"{result:.2f}")
    elif txt == 'string':

        text_result = f"${number}$"
        print(text_result)


type_text = input()
item = input()
data_types(type_text, item)