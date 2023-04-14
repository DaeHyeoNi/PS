import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
accumulated = [0]

temp = 0
for i in numbers:
    temp += i
    accumulated.append(temp)

for i in range(M):
    a, b = map(int, input().split())
    print(accumulated[b] - accumulated[a-1])