import sys

def solution():
    input = sys.stdin.readline
    n, e = map(int, input().split())

    choo = list(map(int, input().split()))
    choo.sort()
    
    i = 0
    material_count = 1

    while True:
        if i+1 == n:
            break
        if choo[i+1] - choo[i] >= e:
            material_count += 1
        i += 1

    print(material_count)


if __name__ == "__main__":
    solution()
