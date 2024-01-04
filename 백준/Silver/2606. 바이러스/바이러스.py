computer = int(input())
network = int(input())
graph = [[] for _ in range(computer + 1)]

for _ in range(network):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer + 1)

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때
visited[1] = True
queue = [1]

count = 0
while queue:
    node = queue.pop(0)
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True

            # 새로 방문한 노드를 큐에 추가
            # 이는 다음 반복문에서 인접한 컴퓨터를 감염시키기 위함
            queue.append(i)
            count += 1
print(count)
