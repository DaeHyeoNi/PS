target_num = int(input())

memo = {
    0: 0,
    1: 1,
    2: 1,
}


def fibonacci_memo(n):
    if n <= 2:
        return memo[n]
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    import time

    start = time.time()
    fibo = fibonacci_memo(target_num)
    print("1 : ", fibo, "elapsed: ", time.time() - start)

    start = time.time()
    fibo = fibonacci(target_num)
    elapsed = time.time() - start
    print("2 : ", fibo, "elapsed: ", elapsed)

    """
        target_num = 35
        1 :  9227465 elapsed:  5.602836608886719e-05 (0.00005603s)
        2 :  9227465 elapsed:  11.956724166870117
    """
