graph = {}

for _ in range(12):
    x, y = input().split()
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []

    graph[x].append(y)
    graph[y].append(x)

three = []
for node, edges in graph.items():
    if len(edges) == 3:
        three.append(node)


for node in three:
    total = 0
    for connected_node in graph[node]:
        total += len(graph[connected_node])
    if total == 6:
        print(node)
        break
