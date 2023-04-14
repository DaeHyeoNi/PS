import sys

input = sys.stdin.readline

N, M = map(int, input().split())

storage = {}

for _ in range(N):
    site, password = input().split()
    storage[site] = password

for _ in range(M):
    site = input().strip()
    print(storage[site])
