grid, moves = [lines.strip() for lines in open("input15.txt").read().split("\n\n")]
big_grid = grid.replace("#", "##")
big_grid = big_grid.replace("O", "[]")
big_grid = big_grid.replace(".", "..")
big_grid = big_grid.replace("@", "@.")

grid = {(i+j*1j):c for i, r in enumerate(grid.split())
                 for j, c in enumerate(r.strip())}
moves = moves.replace("\n", "")

pos = [k for k, v in grid.items() if v == "@"][0]
grid[pos] = "."

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

def big_walk(pos, move):
    if big_grid[pos + move] == "#":
        return pos
    if big_grid[pos + move] == ".":
        return pos + move

    moves = []
    if move in [-1j, 1j]:
        while big_grid[pos + (move * (len(moves) + 1))] in "[]":
            moves.append(pos + (move * (len(moves) + 1)))
        if big_grid[pos + (move * (len(moves) + 1))] == ".":
            for box in moves[::-1]:
                big_grid[box + move] = big_grid[box]
            big_grid[pos + move] = "."
        else:
            return pos #000@ < don't move

    else:
        # there is a box above or beneath, now start the hard part
        # first add the first box
        match big_grid[pos + move]:
            case "[":
                moves.extend([pos + move, pos + move + 1j])
            case "]":
                moves.extend([pos + move, pos + move - 1j])
        while True: # start a loop
            if any(big_grid[box + move] == "#" for box in moves if box + move not in moves):
                return pos
            if all(big_grid[box + move] == "." for box in moves if box + move not in moves):
                # start moving up or down
                while moves:
                    for box in moves[:]:
                        if box + move in moves:
                            continue
                        big_grid[box + move] = big_grid[box]
                        big_grid[box] = "."
                        moves.remove(box)
                return pos + move
            # add extra boxes to moves
            for box in moves[:]:
                if box + move in moves:
                    continue
                match big_grid[box + move]:
                    case "[":
                        moves.extend([box + move, box + move + 1j])
                    case "]":
                        moves.extend([box + move, box + move - 1j])



    return pos + move

dirs = {"^": -1, ">": 1j, "v": 1, "<": -1j}
nr = 0
for move in moves:
    nr += 1
    pos = walk(pos, dirs[move])

answer1 = 0
for k, v in grid.items():
    if v == "O":
        answer1 += k.real * 100 + k.imag
print(int(answer1))

nr = 0
big_grid = {(i+j*1j):c for i, r in enumerate(big_grid.split())
                 for j, c in enumerate(r.strip())}
pos = [k for k, v in big_grid.items() if v == "@"][0]
big_grid[pos] = "."
for move in moves:
    nr += 1
    pos = big_walk(pos, dirs[move])

answer2 = 0
for k, v in big_grid.items():
    if v == "[":
        answer2 += k.real * 100 + k.imag
print(int(answer2))
