import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))
    uniq_sorted = sorted(set(arr))
    rank = {v: i for i, v in enumerate(uniq_sorted)}
    print(' '.join(str(rank[x]) for x in arr))


if __name__ == "__main__":
    solve()
