white_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

black_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]


n, m = map(int, input().split())
board = [input() for _ in range(n)]


def check(i, j):
    result_white = 0
    result_black = 0

    for dis_i in range(8):
        for dis_j in range(8):
            now_i, now_j = i + dis_i, j + dis_j
            if board[now_i][now_j] != white_board[dis_i][dis_j]:
                result_white += 1
            if board[now_i][now_j] != black_board[dis_i][dis_j]:
                result_black += 1

    return min(result_white, result_black)


result = 100000000
for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, check(i, j))

print(result)
