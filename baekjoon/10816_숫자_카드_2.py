cards = {}
cnt = int(input())
data = list(map(int, input().split()))
for i in data:
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

cnt = int(input())
data = list(map(int, input().split()))

for i in data:
    if i in cards:
        print(cards[i], end=" ")
    else:
        print(0, end=" ")
