data = {chr(97 + i): i + 1 for i in range(26)}

N = int(input())
hash = list(input())

result = 0
for i in range(N):
    result += data[hash[i]] * (31**i)
print(result % 1234567891)
