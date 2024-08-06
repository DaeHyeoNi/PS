def solution(n, h, v):
    if n / 2 > h:
        h = n - h
    if n / 2 > v:
        v = n - v
    return h * v * 4

n, h, v = map(int, input().split())
print(solution(n, h, v))