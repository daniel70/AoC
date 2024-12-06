lines = open("input04.txt").read().strip().split("\n")
answer1 = answer2 = 0
length, height = len(lines[0]), len(lines)

for x in range(length):
    for y in range(height):
        if lines[y][x] == "X":
            answer1 += 1 if length - x > 3 and lines[y][x + 1] + lines[y][x + 2] + lines[y][x + 3] == "MAS" else 0 # E
            answer1 += 1 if x >= 3 and lines[y][x - 1] + lines[y][x - 2] + lines[y][x - 3] == "MAS" else 0 # W
            answer1 += 1 if height - y > 3 and lines[y + 1][x] + lines[y + 2][x] + lines[y + 3][x] == "MAS" else 0 # S
            answer1 += 1 if y >= 3 and lines[y - 1][x] + lines[y - 2][x] + lines[y - 3][x] == "MAS" else 0 # N
            answer1 += 1 if height - y > 3 and length - x > 3 and lines[y + 1][x + 1] + lines[y + 2][x + 2] + lines[y + 3][x + 3] == "MAS" else 0 # SE
            answer1 += 1 if height - y > 3 and x >= 3 and lines[y + 1][x - 1] + lines[y + 2][x - 2] + lines[y + 3][x - 3] == "MAS" else 0 # SW
            answer1 += 1 if y >= 3 and length - x > 3 and lines[y - 1][x + 1] + lines[y - 2][x + 2] + lines[y - 3][x + 3] == "MAS" else 0 # NE
            answer1 += 1 if y >= 3 and x >= 3 and lines[y - 1][x - 1] + lines[y - 2][x - 2] + lines[y - 3][x - 3] == "MAS" else 0 # NW

        if lines[y][x] == "A" and 1 <= x < length-1 and 1 <= y < height-1:
            NE = {lines[y-1][x-1], lines[y+1][x+1]}
            SW = {lines[y-1][x+1], lines[y+1][x-1]}
            if NE == SW == {'M', 'S'}:
                answer2 += 1

print("answer 1:", answer1)
print("answer 2:", answer2)
