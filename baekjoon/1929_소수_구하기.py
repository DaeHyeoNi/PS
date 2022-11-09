def isPrimeNumber(num):
    last = int(num ** (1 / 2))
    for i in range(2, last + 1):
        if num % i == 0:
            return False

    return True


m, n = map(int, input().split())
for i in range(m, n + 1):
    if isPrimeNumber(i):
        print(i)
