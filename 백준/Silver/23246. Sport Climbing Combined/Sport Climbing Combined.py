runner_cnt = int(input())

runners = []

for i in range(runner_cnt):
    person, lead, speed, bouldering = map(int, input().split())
    score = lead * speed * bouldering
    score_sort_key = lead + speed + bouldering
    runners.append((person, score, score_sort_key))

runners.sort(key=lambda x: (x[1], x[2], x[0]))

print(' '.join(str(x[0]) for x in runners[:3]))
