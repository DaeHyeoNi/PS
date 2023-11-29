import sys
from collections import deque


input = sys.stdin.readline

M, N = map(int, input().split())
q = deque()

tomatos = []
for _ in range(N):
    tomatos.append(list(map(int, input().split())))
    # 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            q.append((i, j))


def bfs(tomatos, M, N):
    while q:
        x, y = q.popleft()

        # 상하좌우로 움직여서 익지 않은 토마토가 있으면 익히기
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy

            # 움직였을때 범위를 벗어나는지 확인
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 익지 않는 토마토가 있으면 익히기
            if tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1  # 일수를 더해줌
                q.append((nx, ny))  # 다음 차례에 익히기 위해 큐에 넣기

    max_day = 0
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                return -1
            max_day = max(max_day, tomatos[i][j])
    return max_day - 1


print(bfs(tomatos, M, N))
