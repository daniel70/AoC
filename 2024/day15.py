grid, moves = [lines.strip() for lines in open("input15.txt").read().split("\n\n")]

grid = {(i+j*1j):c for i, r in enumerate(grid.split())
                 for j, c in enumerate(r.strip())}
moves = moves.replace("\n", "")

pos = [k for k, v in grid.items() if v == "@"][0]
grid[pos] = "."

# def print_grid(grid, pos, move, nr):
#     print("rounde:", nr, move)
#     nl = 0
#     for k, v in grid.items():
#         nl += 1
#         if k == pos:
#             print("@", end="")
#         else:
#             print(v, end="")
#         if nl % 10 == 0:
#             print("")

def walk(pos, move):
    if grid[pos + move] == "#":
        return pos
    if grid[pos + move] == ".":
        return pos + move

    moves = []
    while grid[pos + (move * (len(moves) + 1))] == "O":
        moves.append(pos + (move * (len(moves) + 1)))
    if grid[pos + (move * (len(moves) + 1))] == ".":
        for box in moves[::-1]:
            grid[box + move] = "O"
        grid[pos + move] = "."
    else:
        return pos #000@ < don't move

    return pos + move

dirs = {"^": -1, ">": 1j, "v": 1, "<": -1j}
nr = 0
for move in moves:
    nr += 1
    # print_grid(grid, pos, move, nr)
    pos = walk(pos, dirs[move])

answer1 = 0
for k, v in grid.items():
    if v == "O":
        answer1 += k.real * 100 + k.imag
print(int(answer1))

