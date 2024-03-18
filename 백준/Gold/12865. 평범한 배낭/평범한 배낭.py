max_cnt, max_weight = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(max_cnt)]

# dp 테이블 초기화: (max_cnt+1) x (max_weight+1) 크기, 모든 값은 0
dp = [[0 for _ in range(max_weight + 1)] for _ in range(max_cnt + 1)]

# DP를 이용한 배낭 문제 해결
for i in range(1, max_cnt + 1):
    for w in range(1, max_weight + 1):
        # 현재 아이템(i-1)을 넣을 수 있는 경우
        if items[i-1][0] <= w:
            # 현재 아이템을 넣는 경우와 넣지 않는 경우 중 최대 가치 선택
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][0]] + items[i-1][1])
        else:
            # 현재 아이템을 넣을 수 없는 경우, 이전 아이템의 가치를 그대로 사용
            dp[i][w] = dp[i-1][w]

# 최대 가치 출력
print(dp[max_cnt][max_weight])
