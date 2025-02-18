n = 10000
a = [False,False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(n//2, 1, -1):
        if a[i] and a[n-i]:
            print(i, n-i)
            break