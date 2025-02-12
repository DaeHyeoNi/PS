method, s = map(str, input().split())


if method == 'E':
    before = None
    stack = 1

    res = ''

    for i in s:
        if before == i:
            stack += 1
        elif before == None:
            pass
        else:
            res += f'{before}{stack}'
            stack = 1
        before = i
    
    res += f'{before}{stack}'

    print(res)

elif method == 'D':
    res = ''
    for i in range(0, len(s), 2):
        string, loop_cnt = s[i], s[i+1]
        res += string * int(loop_cnt)

    print(res)
