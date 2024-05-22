import math


def closest_point(x1, y1, x2, y2):
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if distance1 <= distance2:
        print(f"({x1}, {y1})")
    else:
        print(f"({x2}, {y2})")


X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
closest_point(X1, Y1, X2, Y2)

