paper = [[0]*100 for _ in range(100)]

color_paper_count = int(input())

for _ in range(color_paper_count):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

result = 0

for i in range(100):
    result += sum(paper[i])

print(result)