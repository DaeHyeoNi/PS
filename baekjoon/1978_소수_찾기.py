def isPrimeNumber(num):
    if num == 1:
        return False
    last = int(num ** (1 / 2))
    for i in range(2, last + 1):
        if num % i == 0:
            return False

    return True


n = int(input())
numbers = map(int, input().split())
sum = 0
for number in numbers:
    if isPrimeNumber(number):
        sum += 1

print(sum)
