number_of_balls = int(input())

best_ball = 0
best_weight = 0
best_time = 0
best_quality = 0
best_formula = 0

for _ in range(number_of_balls):

    weight = int(input())
    time = int(input())
    quality = int(input())

    formula = (weight / time) ** quality

    if best_ball < formula:
        best_ball = formula
        best_weight = weight
        best_time = time
        best_quality = quality
        best_formula = formula


print(f"{best_weight} : {best_time} = {int(best_formula)} ({best_quality})")
