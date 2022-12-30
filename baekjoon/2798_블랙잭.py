from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))

big = 0

for cards in combinations(card_list, 3):
    temp = sum(cards)
    if big < temp <= M:
        big = temp

print(big)
