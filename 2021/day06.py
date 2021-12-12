from collections import Counter

init = list(map(int, open('input06.txt').read().split(",")))
c = Counter(init)

for i in range(256):
    if i == 80:
        print('answer 1:', sum(c.values()))

    new_fish = c[0]
    for day in range(8):
        c[day] = c[day+1]
    c[6] += new_fish
    c[8] = new_fish

print('answer 2:', sum(c.values()))