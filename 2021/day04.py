first = False
boards = []
board = []
numbers = []
winners = set()
stop = False
with open('input04.txt') as f:
    numbers = [int(nr.strip()) for nr in f.readline().strip().split(",")]
    for line in f:
        line = line.strip()
        if not line:
            if board:
                boards.append(board)
            board = []
        else:
            board.append([int(x) for x in line.split()])
    boards.append(board)

for nr in numbers:
    winners = set()
    for board in boards:
        for row in board:
            try:
                i = row.index(nr)
                row[i] = -1
            except ValueError as e:
                pass

    # check the boards for bingo
    # horizontally
    for bidx, board in enumerate(boards):
        for ridx, row in enumerate(board):
            if sum(row) == -5:
                winners.add(bidx)

    # vertically
    for bidx, board in enumerate(boards):
        for i in range(5):
            if sum([board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]) == -5:
                winners.add(bidx)

    if winners and not first:
        total = 0
        first = True
        for row in boards[list(winners)[0]]:
            total += sum([c for c in row if c > 0])
        print(f'answer 1: {total * nr}')

    if winners:
        for w in sorted(winners, reverse=True):
            if len(boards) > 1:
                del boards[w]
            else:
                stop = True

    if stop:
        break

total = 0
for row in boards[0]:
    total += sum([c for c in row if c > 0])
print(f'answer 2: {total * nr}')
