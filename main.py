import matplotlib.pyplot as plt

n, m = 60, 60

board = []
visited = []

for i in range(n):
    board.append([])
    visited.append([])
    for j in range(m):
        board[i].append(0)
        visited[i].append(False)

point = (n // 2, m // 2)
current_view = 1

for i in range(n * m - 1):
    board[point[0]][point[1]] = i + 1
    if current_view == 0:
        point = (point[0] + 1, point[1])
        if board[point[0]][point[1] - 1] == 0:
            current_view = 1
    elif current_view == 1:
        point = (point[0], point[1] - 1)
        if board[point[0] - 1][point[1]] == 0:
            current_view = 2
    elif current_view == 2:
        point = (point[0] - 1, point[1])
        if board[point[0]][point[1] + 1] == 0:
            current_view = 3
    elif current_view == 3:
        point = (point[0], point[1] + 1)
        if board[point[0] + 1][point[1]] == 0:
            current_view = 0

board[point[0]][point[1]] = n * m


def generate_valid_knight_moves(board_tmp, position):
    moves = []
    if position[0] - 2 >= 0 and position[1] - 1 >= 0:
        moves.append((position[0] - 2, position[1] - 1))
    if position[0] - 2 >= 0 and position[1] + 1 < len(board_tmp[0]):
        moves.append((position[0] - 2, position[1] + 1))
    if position[0] + 2 < len(board_tmp) and position[1] - 1 >= 0:
        moves.append((position[0] + 2, position[1] - 1))
    if position[0] + 2 < len(board_tmp) and position[1] + 1 < len(board_tmp[0]):
        moves.append((position[0] + 2, position[1] + 1))
    if position[0] - 1 >= 0 and position[1] - 2 >= 0:
        moves.append((position[0] - 1, position[1] - 2))
    if position[0] - 1 >= 0 and position[1] + 2 < len(board_tmp[0]):
        moves.append((position[0] - 1, position[1] + 2))
    if position[0] + 1 < len(board_tmp) and position[1] - 2 >= 0:
        moves.append((position[0] + 1, position[1] - 2))
    if position[0] + 1 < len(board_tmp) and position[1] + 2 < len(board_tmp[0]):
        moves.append((position[0] + 1, position[1] + 2))

    return moves


starting_position = (n // 2, m // 2)
current_position = starting_position
possible_moves = generate_valid_knight_moves(board, current_position)
path = [starting_position]
visited[starting_position[0]][starting_position[1]] = True
while len(possible_moves) > 0:
    min_move = ((-1, -1), 1000000000000)
    for move in possible_moves:
        if board[move[0]][move[1]] < min_move[1] and not visited[move[0]][move[1]]:
            min_move = (move, board[move[0]][move[1]])
    if min_move[0] == (-1, -1):
        print("No more moves")
        break
    current_position = min_move[0]
    path.append(current_position)
    visited[current_position[0]][current_position[1]] = True
    possible_moves = generate_valid_knight_moves(board, current_position)

print(path)

ans: int = int(input("1. Save as image\n2. Show the image\n3. Save the cool transparent image version\n"))

if ans == 1:
    plt.plot([x[0] - n // 2 for x in path], [x[1] - m // 2 for x in path], c="Black", linewidth=0.5)
    plt.savefig("knight.png", transparent=False, dpi=500)
if ans == 2:
    plt.plot([x[0] - n // 2 for x in path], [x[1] - m // 2 for x in path], c="Black", linewidth=0.5)
    plt.show()
if ans == 3:
    # Plot the path
    plt.plot([x[0] - n // 2 for x in path], [x[1] - m // 2 for x in path], c="lawngreen", linewidth=0.5)
    plt.axis("off")
    for i in range(n):
        plt.scatter([i - n // 2 for j in range(m)], [j - m // 2 for j in range(m)], c="white", s=0.1)
    plt.savefig("knight.png", transparent=True, dpi=500)

