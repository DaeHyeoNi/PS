N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

# 탐색을 완료하면 반복 종료
while start <= end:
    # 나무의 평균 값을 중앙값으로 둔다
    mid = (start + end) // 2
    cut_length = 0

    # 중앙값보다 긴 나무가 있으면 자른 길이에 포함
    for tree in trees:
        if tree >= mid:
            cut_length += tree - mid

    # 자른 길이가 길거나 작을때 탐색범위를 줄인다
    if cut_length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
