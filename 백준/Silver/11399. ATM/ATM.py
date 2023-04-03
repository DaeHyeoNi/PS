n = int(input())
humans = map(int, input().split())
humans = sorted(humans)

sum = 0

for i in range(n):
    for j in range(i + 1):
        sum += humans[j]

print(sum)