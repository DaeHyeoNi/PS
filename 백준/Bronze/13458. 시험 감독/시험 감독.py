import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

def solution(n, b, c, a):
    count = 0
    for i in range(n):
        # 각 시험장에 총감독관 1명 배치
        count += 1
        remaining = a[i] - b
        
        # 남은 응시자가 있다면 부감독관 배치
        if remaining > 0:
            count += (remaining + c - 1) // c  # 올림 나눗셈
            
    return count

print(solution(n, b, c, a))