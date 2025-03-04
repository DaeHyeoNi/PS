height = int(input())
cookie = []

for i in range(height):
    data = []
    c = input()
    for j in c:
        if j == '*':
            data.append(1)
        elif j == '_':
            data.append(0)
        else:
            raise ValueError()
    cookie.append(data)

# Initialize positions and lengths
head_pos = None
heart_pos = None
left_arm_len = 0
right_arm_len = 0
waist_len = 0
left_leg_len = 0
right_leg_len = 0

for i in range(height):
    for j in range(len(cookie[i])):
        if cookie[i][j] == 1:
            if head_pos is None:
                head_pos = (i, j)
                heart_pos = (i + 1, j)
                break


heart_row = heart_pos[0]
heart_col = heart_pos[1]

# Calculate arm lengths
for j in range(heart_col - 1, -1, -1):
    if j < 0 or j >= len(cookie[heart_row]) or cookie[heart_row][j] == 0:
        break
    left_arm_len += 1

for j in range(heart_col + 1, len(cookie[heart_row])):
    if j >= len(cookie[heart_row]) or cookie[heart_row][j] == 0:
        break
    right_arm_len += 1

# Calculate waist length
waist_row = heart_row + 1
while waist_row < height:
    if waist_row >= height or cookie[waist_row][heart_col] == 0:
        break
    # Check if this is where legs branch out (cells to left and right are filled)
    left_pos = heart_col - 1
    right_pos = heart_col + 1
    if (left_pos >= 0 and left_pos < len(cookie[waist_row]) and cookie[waist_row][left_pos] == 1) or \
       (right_pos < len(cookie[waist_row]) and cookie[waist_row][right_pos] == 1):
        break
    waist_len += 1
    waist_row += 1

# Calculate leg starting positions based on waist
leg_start_row = heart_row + 1 + waist_len
left_leg_col = heart_col - 1
right_leg_col = heart_col + 1

# Calculate leg lengths
for i in range(leg_start_row, height):
    if i >= height or left_leg_col < 0 or left_leg_col >= len(cookie[i]) or cookie[i][left_leg_col] == 0:
        break
    left_leg_len += 1

for i in range(leg_start_row, height):
    if i >= height or right_leg_col < 0 or right_leg_col >= len(cookie[i]) or cookie[i][right_leg_col] == 0:
        break
    right_leg_len += 1

# Print results
print(f"{heart_pos[0] + 1} {heart_pos[1] + 1}")
print(left_arm_len, right_arm_len, waist_len, left_leg_len, right_leg_len)
