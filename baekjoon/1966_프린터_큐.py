N = int(input())

for _ in range(N):
    document_cnt, query = map(int, input().split())
    priority = list(map(int, input().split()))

    cnt = 0

    while query != -1:
        if priority[0] == max(priority):
            priority.pop(0)
            query -= 1
            cnt += 1
        else:
            priority.append(priority.pop(0))

            if query == 0:
                query = len(priority) - 1
            else:
                query -= 1

    print(cnt)
