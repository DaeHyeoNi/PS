N = int(input())
result = 0
for i in range(1, N + 1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i

    if result == N:
        print(i)
        break
    elif i == N:
        print(0)
