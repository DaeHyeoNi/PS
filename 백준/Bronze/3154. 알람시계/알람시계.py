import sys

# 숫자 키패드 좌표 (맨해튼 거리 계산용)
# 1 2 3
# 4 5 6
# 7 8 9
#   0
coords = {
    1: (0, 0), 2: (1, 0), 3: (2, 0),
    4: (0, 1), 5: (1, 1), 6: (2, 1),
    7: (0, 2), 8: (1, 2), 9: (2, 2),
    0: (1, 3)
}

def effort(a, b):
    x1, y1 = coords[a]
    x2, y2 = coords[b]
    return abs(x1 - x2) + abs(y1 - y2)

def solve(target_h, target_m):
    best = None
    best_eff = float('inf')

    # 시 후보 (0~99 중 target_h ≡ h mod 24)
    hours = []
    for k in range(0, (99 - target_h) // 24 + 1):
        h = target_h + 24 * k
        hours.append(h)

    # 분 후보 (0~99 중 target_m ≡ m mod 60)
    minutes = []
    for k in range(0, (99 - target_m) // 60 + 1):
        m = target_m + 60 * k
        minutes.append(m)

    for h in hours:
        d0, d1 = divmod(h, 10)
        for m in minutes:
            d2, d3 = divmod(m, 10)
            e = effort(d0, d1) + effort(d1, d2) + effort(d2, d3)
            key = (h, m)
            if e < best_eff or (e == best_eff and key < best):
                best_eff = e
                best = key

    return best

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    H, M = map(int, line.split(":"))
    h_ans, m_ans = solve(H, M)
    print(f"{h_ans:02d}:{m_ans:02d}")