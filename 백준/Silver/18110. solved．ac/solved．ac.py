import sys
input = sys.stdin.readline

def round45(n):
    return int(n) + 1 if n % 1 >= 0.5 else int(n)

def solution(n):
    if n == 0:
        return 0

    scores = []

    for _ in range(n):
        scores.append(int(input()))
    
    scores.sort()
    trun = round45(n * 0.15)
    
    res = 0
    for i in range(trun, n - trun):
        res += scores[i]
    
    return round45(res / (n - trun * 2))

print(solution(int(input())))