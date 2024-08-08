p = ''
for i in range(1, 100001):
    p += str(i)

print(p.index(str(input()))+1)
