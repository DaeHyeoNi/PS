from collections import deque

def command_runner(p, nums):
    queue = deque(nums)
    is_reversed = False

    for command in p:
        if command == 'R':
            is_reversed = not is_reversed
        else:
            if len(queue) == 0:
                return 'error'
            elif is_reversed:
                queue.pop()
            else:
                queue.popleft()

    if is_reversed:
        queue.reverse()
    
    return list(queue)

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    x = input()[1:-1]
    nums = x.split(',')

    if n == 0:
        nums = []

    result = command_runner(p, nums)

    if result == 'error':
        print('error')
    else:
        print('[' + ','.join(result) + ']')
