import sys

FACTORIALS = [1]  # 0!
for i in range(1, 11):
    FACTORIALS.append(FACTORIALS[-1] * i)

def solution(num: int):
    s = list(str(num))
    
    ans = 0
    for i in range(len(s)):
        ans += int(s[i]) * FACTORIALS[len(s)-i]
    return ans

while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    print(solution(a))