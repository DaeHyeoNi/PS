import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = defaultdict(int)   # 윈도우 내 과일별 개수
left = 0
kinds = 0                # 서로 다른 과일 종류 수
ans = 0

for right, x in enumerate(arr):
    if cnt[x] == 0:
        kinds += 1
    cnt[x] += 1

    # 조건 위반 시: 왼쪽을 당겨서 종류 수를 2 이하로 만든다
    while kinds > 2:
        y = arr[left]
        cnt[y] -= 1
        if cnt[y] == 0:
            kinds -= 1
        left += 1

    # 현재 윈도우 길이로 최댓값 갱신
    ans = max(ans, right - left + 1)

print(ans)
