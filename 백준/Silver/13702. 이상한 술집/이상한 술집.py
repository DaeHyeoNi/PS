import sys
input = sys.stdin.readline

n, k = map(int, input().split())

kettles = []
for _ in range(n):
    kettles.append(int(input()))

start = 1
end = max(kettles)

ans = 0
while start <= end:
    mid = (start + end) // 2
    count = 0

    count = sum(kettle // mid for kettle in kettles)

    if count >= k:
        ans = mid
        start = mid + 1  # 나눠줄 수 있으면 더 큰 값으로 나눠줘야 함
    else:
        # 못 나눠주면 더 작은 값으로 나눠줘야 함
        end = mid - 1

print(ans)
