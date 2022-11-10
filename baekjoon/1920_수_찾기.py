N = int(input())
line1 = set(map(int, input().split()))
M = int(input())
line2 = list(map(int, input().split()))

# 제출 이후 PASS를 하긴 했는데 알고리즘 분류가
# 정렬, 이분탐색인걸 보니 이분탐색이 정식풀이법인듯

for i in line2:
    if i in line1:
        print(1)
    else:
        print(0)
