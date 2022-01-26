from collections import namedtuple

rules = []
Rule = namedtuple("Rule", "low high")
for low, high in [line.strip().split("-") for line in open("input20.txt").readlines()]:
    rules.append(Rule(int(low), int(high)))
rules.sort(key=lambda rule: rule.low)

low = high = 0
for rule in rules:
    if low < rule.low:
        print(low)
        break
    high = max(high, rule.high)
    low = high + 1

else:
    print(high + 1)

# 1847081 too low
