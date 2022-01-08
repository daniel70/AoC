answer1 = ""
answer2 = ""
lines = open("input06.txt").read().splitlines()
length = len(lines[0])
for idx in range(length):
    letters = []
    for line in lines:
        letters.append(line[idx])

    answer1 += max(letters, key=letters.count)
    answer2 += min(letters, key=letters.count)

print("answer 1:", answer1)
print("answer 2:", answer2)
