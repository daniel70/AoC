import collections as cs
twos: int = 0
threes: int = 0
with open('input02.txt') as f:
    for line in f:
        counts = cs.Counter(line).values()
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
print(f'{twos} twos x {threes} threes = {twos*threes}')
