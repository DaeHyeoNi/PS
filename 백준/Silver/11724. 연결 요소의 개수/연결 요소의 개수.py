import sys

def count_components(n, edges):
    adj = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    visited = set()
    comp = 0

    for start in range(1, n + 1):
        if start in visited:
            continue
        comp += 1
        stack = [start]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)

            # 인접 노드 방문
            for nxt in adj[cur]:
                if nxt not in visited:
                    stack.append(nxt)
    return comp


if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N, M = int(next(it)), int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(M)]
    print(count_components(N, edges))
