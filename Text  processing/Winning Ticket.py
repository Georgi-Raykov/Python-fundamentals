tickets = [x.strip() for x in input().split(',')]

for ticket in tickets:
    symbols = '#@$'
    if len(ticket) < 20 or len(ticket) > 20:
        print('Invalid ticket')
        continue
    is_match = list(filter(lambda x: x == '#' or x == '$' or x == '@', ticket))
    if not is_match:
        print(f"ticket {ticket} - no match")
        continue

    str_ticket = ''.join(ticket)
    first_half = str_ticket[0:10]
    second_half = str_ticket[10:]

    first = []
    second = []
    symbol = ''
    for i in range(len(first_half)):
        if 0 <= i < len(first_half):
            if first_half[i] in symbols:
                symbol = first_half[i]
                if first_half[i] == symbol:
                    first.append(first_half[i])

            if second_half[i] in symbols:
                symbol = second_half[i]
                if second_half[i] == symbol:
                    second.append(second_half[i])
    if len(first) >= 6 and len(second) >= 6:
        six = 6
        print(f"ticket {ticket} - {six}{symbol}")
    elif len(first) == 10 and len(second) == 10:
        print(f"ticket {ticket} - {len(first_half)}{symbol} Jackpot!")
