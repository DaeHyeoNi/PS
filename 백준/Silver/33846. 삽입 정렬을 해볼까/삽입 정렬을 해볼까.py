import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))

# 꼼수
arr[:t] = sorted(arr[:t])

print(' '.join(map(str, arr)))
