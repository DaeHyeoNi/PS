import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if visited[x][y]:
        return
    if matrix[x][y] != color:
        return
    visited[x][y] = True
    dfs(x + 1, y, color)
    dfs(x - 1, y, color)
    dfs(x, y + 1, color)
    dfs(x, y - 1, color)


def solve():
    answer = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, matrix[i][j])
                answer += 1
    return answer



answers = [0, 0]
answers[0] = solve()

# 적록색약인 사람이 봤을 때의 구역의 수
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "G":
            matrix[i][j] = "R"

visited = [[False] * n for _ in range(n)]
answers[1] = solve()

print(answers[0], answers[1])