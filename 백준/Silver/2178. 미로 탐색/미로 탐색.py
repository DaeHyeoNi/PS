from collections import deque


N, M = map(int, input().split())  # 미로의 세로 크기 N, 가로 크기 M을 입력받음
maze = [list(map(int, input())) for _ in range(N)]  # 미로 정보를 입력받음


def bfs(maze):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N - 1][M - 1]


print(bfs(maze))
