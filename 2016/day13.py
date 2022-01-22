import collections as co

LRUD = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # look left, right, up and down
special_number = 1350
endpoint = (31, 39)
answer1 = answer2 = 0


def is_space(x: int, y: int) -> bool:
    return bin(x*x + 3*x + 2*x*y + y + y*y + special_number).count('1') % 2 == 0


moves = co.defaultdict(list)
moves[0].append((1, 1))
seen = set((1, 1))
while True:
    last_step = max(moves)
    if endpoint in moves[last_step]:
        answer1 = last_step
        break

    step = last_step + 1
    if step == 50:
        answer2 = len(seen)

    for pos in moves[last_step]:
        x, y = pos
        for new in [(x + dx, y + dy) for dx, dy in LRUD if x + dx >= 0 and y + dy >= 0]:
            if is_space(*new) and new not in seen:
                moves[step].append(new)
                seen.add(new)

print("answer 1:", answer1)
print("answer 2:", answer2)
