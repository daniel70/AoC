instructions = []
with open('input01.txt') as f:
    for line in f:
        line = line.strip()
        instructions.append(line)

totals = []
sum_calories = 0
for calories in instructions:
    if calories:
        sum_calories += int(calories)
    else:
        totals.append(sum_calories)
        sum_calories = 0

totals.sort(reverse=True)
print("answer 1:", totals[0])
print("answer 2:", sum(totals[:3]))
