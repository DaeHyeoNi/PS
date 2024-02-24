import sys

input = sys.stdin.readline

target = int(input())
int(input())
blocked_number = list(map(int, input().split()))


# 수빈이가 지금 보고 있는 채널
min_count = abs(100 - target)

for nums in range(1000000):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in blocked_number:
            break

        elif j == len(nums) - 1:
            min_count = min(min_count, abs(target - int(nums)) + len(str(nums)))

print(min_count)
