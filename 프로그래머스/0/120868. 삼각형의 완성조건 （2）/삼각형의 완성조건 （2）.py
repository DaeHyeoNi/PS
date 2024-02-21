def solution(sides):
    a, b = sides[0], sides[1]

    min_length = abs(a - b) + 1

    max_length = a + b - 1

    possible_lengths = max_length - min_length + 1
    return possible_lengths