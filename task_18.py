way = {1:0, 2:1, 3:1, 4:0, 5:0,
       6:0, 7:-0, 8:0, 9:0, 10:0}

mountain = 0
valley = 0
for step in way.values():
    if abs(step) > 0:
        mountain += step
    else:
        valley += (step+1)
    print(step)
print("Пройдено {} долин.".format(abs(valley)))
print("Пройдено {} гор.".format(mountain))
