# fmt: off
import sys
input, N, coords = sys.stdin.readline, int(input()), []
[coords.append(list(map(int, input().split()))) for _ in range(N)]
[print(f'{coord[0]} {coord[1]}') for coord in sorted(coords, key=lambda x: (x[0], x[1]))]
