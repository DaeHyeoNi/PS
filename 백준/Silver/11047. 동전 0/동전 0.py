n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)
cnt = 0
for c in coin:
    if k == 0:
        break
    cnt += k // c
    k %= c

print(cnt)