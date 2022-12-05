N = int(input())
stack_target = []
ans = []
count = 1
find = True
for _ in range(N):
    num = int(input())
    while count <= num:
        stack_target.append(count)
        ans.append("+")
        count += 1
    if stack_target[-1] == num:
        stack_target.pop()
        ans.append("-")
    else:
        find = False

if not find:
    print("NO")
else:
    for i in ans:
        print(i)
