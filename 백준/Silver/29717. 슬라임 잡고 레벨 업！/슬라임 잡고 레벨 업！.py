# lvup -> n(n+1)/2

T = int(input())
for _ in range(T):
    N = int(input())
    slime_exp = ((N + 1) * N) // 2
    
    left = 1
    right = 1000000000
    answer = 1
    
    while left <= right:
        level = (left + right) // 2
        need_exp = (level + 1) * level
        
        if need_exp < slime_exp:
            left = level + 1
            answer = max(level + 1, answer)
        elif need_exp > slime_exp:
            right = level - 1
        else:
            answer = level + 1
            break
            
    print(answer)
