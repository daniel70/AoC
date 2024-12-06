from collections import Counter

lines = open("input01.txt").read().strip().split("\n")
lefts = []
rights = []
answer1 = answer2 = 0
for line in lines:
    left, right = line.split()
    lefts.append(int(left))
    rights.append(int(right))

counts = Counter(rights)
for left, right in zip(sorted(lefts), sorted(rights)):
    answer1 += abs(left - right)
    answer2 += (left * counts[left])

print("answer 1:", answer1)
print("answer 2:", answer2)
