import math


def neighbours(i, W):
    return [i + a for a in adjacent if 0 <= i + a < W*H and -1 <= ((i + a) % W) - (i % W) <= 1]


def corners(board, W, H):
    board[0] = True
    board[W - 1] = True
    board[W * H - W] = True
    board[W * H - 1] = True
    return board


def animate(board, corners_are_stuck=False):
    if corners_are_stuck:
        board = corners(board, W, H)

    for i in range(100):
        new_board = board.copy()
        for idx, val in enumerate(board):
            if val and sum([board[cell] for cell in neighbours(idx, W)]) not in [2, 3]:
                new_board[idx] = False
            elif not val and sum([board[cell] for cell in neighbours(idx, W)]) == 3:
                new_board[idx] = True

        board = new_board
        if corners_are_stuck:
            board = corners(board, W, H)

    return board


instructions = []
with open('input18.txt') as f:
    for line in f:
        line = line.strip()
        instructions.extend([p == "#" for p in line])

W = H = int(math.sqrt(len(instructions)))
adjacent = [-W-1, -W, -W+1, -1, 1, W-1, W, W+1]

print("answer 1:", sum(animate(instructions.copy())))
print("answer 2:", sum(animate(instructions.copy(), corners_are_stuck=True)))
