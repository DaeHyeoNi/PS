n = int(input())
animals = []
for _ in range(n):
    animals.append(input())

total = 0
for i in range(n):
    if animals[i] == 'O':
        total += 1 << (n - i - 1)

print(total)
