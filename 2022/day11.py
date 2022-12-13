from collections import deque
from dataclasses import dataclass
from functools import reduce


@dataclass
class Monkey:
    items: deque
    operation: str
    test: int
    true: int
    false: int
    inspections: int = 0


monkeys = []
with open("test11.txt") as f:
    for line in f:
        items = f.readline().strip()[16:]
        operation = f.readline().strip()[17:]
        test = f.readline().strip()[6:]
        true = f.readline().strip()[25:]
        false = f.readline().strip()[26:]
        f.readline()
        monkeys.append(
            Monkey(
                deque(int(item) for item in items.split(",")),
                operation,
                int(test.split()[-1]),
                int(true),
                int(false),
            )
        )

gcd = reduce(lambda x, y: x*y, [m.test for m in monkeys])
for round in range(10_000):
    for m in monkeys:
        while m.items:
            old = m.items.popleft()
            new = eval(m.operation)
            new = new % gcd
            if new % m.test == 0:
                monkeys[m.true].items.append(new)
            else:
                monkeys[m.false].items.append(new)
            m.inspections += 1

    if round == 19:
        sorted_monkeys = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
        print("answer 1:", sorted_monkeys[0].inspections * sorted_monkeys[1].inspections)

sorted_monkeys = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
print("answer 2:", sorted_monkeys[0].inspections * sorted_monkeys[1].inspections)
