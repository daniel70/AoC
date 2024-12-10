import functools

answer1 = answer2 = 0
part1, part2 = open("input05.txt").read().strip().split("\n\n")

rules = []
for rule in part1.split("\n"):
    rules.append([int(i) for i in rule.split("|")])

updates = []
for update in part2.split("\n"):
    updates.append([int(i) for i in update.split(",")])

def compare(x, y):
    if [y, x] in rules:
        return 1
    return -1

for update in updates:
    correct = sorted(update, key=functools.cmp_to_key(compare))
    answer1 += update[len(update)//2] if update == correct else 0
    answer2 += correct[len(correct)//2] if update != correct else 0

print("answer 1:", answer1)
print("answer 2:", answer2)
   