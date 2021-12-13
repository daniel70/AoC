import re

W = H = 0
points = set()
folds = []
with open('input13.txt') as f:
    top = True
    for line in f:
        line = line.strip()
        if not line:
            top = False
            continue
        if top:
            x, y = map(int, line.split(","))
            # x, y = [(int(l[0]), int(l[1])) for l in line.split(",")]
            W = max(W, x)
            H = max(H, y)
            points.add((x, y))
        else:
            m = re.search(r"([xy])=(\d+)", line)
            if m:
                g = m.groups()
                folds.append((g[0], int(g[1])))

W += 1
H += 1
paper = [False] * (W * H)
for x, y in points:
    paper[y * W + x] = True


answer1 = False
for direction, fold_line in folds:
    if direction == 'y':
        start = (fold_line + 1) * W
        for idx, val in enumerate(paper[start:]):
            if val:
                row = (idx // W) + 1
                col = idx % W
                mirror = (fold_line - row) * W + col
                paper[mirror] = True

        # fold & cut
        paper = paper[:fold_line * W]
        H -= H - fold_line
    else:
        for row in range(len(paper) // W):
            for col in range(fold_line + 1, W):
                point = row * W + col
                if paper[point]:
                    mirror = row * W + fold_line - (col - fold_line)
                    paper[mirror] = True

        # fold & cut
        for row in reversed(range(len(paper) // W)):
            paper[row * W + fold_line: row * W + W] = []
        W -= W - fold_line

    if not answer1:
        print(f"answer 1:", sum(paper))
        answer1 = True

# print the final result, this is the answer to question 2:
print("answer 2:")
for row in range(len(paper) // W):
    for col in paper[row * W: row * W + W]:
        if col:
            print("#", end="")
        else:
            print(" ", end="")
    print("")
