def solution(a, b):
    import datetime

    today = datetime.date(a[0], a[1], a[2])
    today_after_1000 = datetime.date(a[0] + 1000, a[1], a[2])
    target = datetime.date(b[0], b[1], b[2])
    dday = (target - today).days

    limit = (today_after_1000 - today).days
    if dday >= limit:
        print("gg")
    else:
        print(f"D-{dday}")


solution(list(map(int, input().split())), list(map(int, input().split())))
