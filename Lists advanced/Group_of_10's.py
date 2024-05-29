def group_by_10(num):
    start = 0
    boundary = 10
    index = 0
    track = []
    while len(num) > 0:

        if start < num[index] <= boundary:
            track.append(num[index])
            num.remove(num[index])
            if len(num) == 0:
                print(f"Group of {boundary}'s: {track}")
        else:
            if index + 1 < len(num):
                index += 1
            else:
                print(f"Group of {boundary}'s: {track}")
                start += 10
                boundary += 10
                index = 0
                track = []


numbers = [int(x) for x in input().split(', ')]
group_by_10(numbers)
