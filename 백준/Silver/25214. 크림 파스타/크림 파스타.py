import sys

_ = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

min_so_far = None
max_diff = 0
ans = []

for x in arr:
    if min_so_far is None:
        min_so_far = x
        max_diff = 0  # x - x = 0
    else:
        max_diff = max(max_diff, x - min_so_far)
        min_so_far = min(min_so_far, x)
    ans.append(max_diff)

print(' '.join(map(str, ans)))
