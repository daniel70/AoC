import itertools

firewall = {}
severity = 0
with open("input13.txt") as f:
    for line in f:
        line.strip()
        layer, depth = [int(x) for x in line.split(": ")]
        firewall[layer] = depth

for layer, depth in firewall.items():
    if layer % (depth * 2 - 2) == 0:
        severity += (layer * depth)

print("answer 1:", severity)

for delay in itertools.count(1):
    for layer, depth in firewall.items():
        if (layer + delay) % (depth * 2 - 2) == 0:
            break
    else:
        break

print("answer 2:", delay)
