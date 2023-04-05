import sys

input = sys.stdin.readline

kv = {}
vk = {}

n, query_cnt = map(int, input().split())

cnt = 1
for i in range(n):
    name = input().rstrip()

    # 포켓몬 이름은 겹치지 않아서 검증 안함
    kv[name] = cnt
    vk[cnt - 1] = name
    cnt += 1

for i in range(query_cnt):
    query = input().rstrip()

    if query.isdigit():
        print(vk[int(query) - 1])
    else:
        print(kv[query])
