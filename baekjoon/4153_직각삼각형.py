while True:
    leg = list(map(int, input().split()))
    leg.sort()
    if leg[0] == 0 and leg[1] == 0 and leg[2] == 0:
        break
    if leg[0] ** 2 + leg[1] ** 2 == leg[2] ** 2:
        print("right")
    else:
        print("wrong")
