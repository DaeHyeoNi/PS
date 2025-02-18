map_size, command_count = map(int, input().split())
map_size += 1

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

current_direction = 0

current_position = [0, 0]

map_data = [[0 for _ in range(map_size)] for _ in range(map_size)]

for _ in range(command_count):
    command = input().split()
    if command[0] == 'MOVE':
        move_count = int(command[1])
        for _ in range(move_count):
            current_position[0] += direction[current_direction][0]
            current_position[1] += direction[current_direction][1]
            if current_position[0] < 0 or current_position[0] >= map_size or current_position[1] < 0 or current_position[1] >= map_size:
                print(-1)
                exit(0)
            map_data[current_position[0]][current_position[1]] += 1
    elif command[0] == 'TURN':
        if command[1] == '0':
            current_direction = (current_direction + 1) % 4
        elif command[1] == '1':
            current_direction = (current_direction + 3) % 4
print(f"{current_position[0]} {current_position[1]}")