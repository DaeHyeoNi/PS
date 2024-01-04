N, r, c = map(int, input().split())

def solve(n, x, y):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    
    if x < half and y < half:
        return solve(n - 1, x, y)
    elif x < half and y >= half:
        return 1 * half * half + solve(n - 1, x, y - half)
    elif x >= half and y < half:
        return 2 * half * half + solve(n - 1, x - half, y)
    else:
        return 3 * half * half + solve(n - 1, x - half, y - half)
    
print(solve(N, r, c))