a = input()

k = a.split('-')

result = sum(map(int, k[0].split('+'))) if '+' in k[0] else int(k[0])

for part in k[1:]:
    if '+' in part:
        result -= sum(map(int, part.split('+')))
    else:
        result -= int(part)

print(result)
