T = int(input())
for i in range(T):
    brace = input()
    last_brace_len = len(brace)
    while True:
        brace = brace.replace("()", "")
        current_brace_len = len(brace)
        if last_brace_len > current_brace_len:
            last_brace_len = current_brace_len
        else:
            break

    if len(brace) == 0:
        print("YES")
    else:
        print("NO")
