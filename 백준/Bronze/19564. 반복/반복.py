target = input()

ans = 0
before = ord(target[0])

for t in target:
    if ord(t) <= before:
        ans += 1
    before = ord(t)

print(ans)
