from collections import namedtuple
ips = 4_294_967_295
rules = []
Rule = namedtuple("Rule", "low high")
for low, high in [line.strip().split("-") for line in open("input20.txt").readlines()]:
    rules.append(Rule(int(low), int(high)))
rules.sort(key=lambda rule: rule.low)
low = high = first = allowed = 0
for rule in rules:
    if low < rule.low:
        if not first:
            first = low
        allowed += rule.low - low

    high = max(high, rule.high)
    low = high + 1

else:
    allowed += ips - min(high, ips)

print("answer 1:", first)
print("answer 2:", allowed)
