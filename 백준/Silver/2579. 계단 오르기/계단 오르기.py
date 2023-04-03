cnt = int(input())
stairs = [int(input()) for _ in range(cnt)]

dp = [0] * cnt

if cnt <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2, cnt):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    
    print(dp[-1])