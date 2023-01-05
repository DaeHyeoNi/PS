test_case = int(input())

for _ in range(test_case):
    H, W, N = map(int, input().split())
    floor = N % H
    ho = N // H + 1
    if floor == 0:
        floor = H
        ho -= 1

    print("{0}{1:02d}".format(floor, ho))
