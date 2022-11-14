# 1 -> 7 -> 19 -> 37 -> 61
#    6   12    18    24
N = int(input())
room_number = 1
passing_count = 1
increase_point = 6
while N > room_number:
    passing_count += 1
    room_number += increase_point
    increase_point += 6
print(passing_count)
