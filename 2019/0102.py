total = 0
# mass = 100756 # 50346
def geerten(m):
    return m // 3 - 2

l = []
with open('input01.txt') as f:
    for line in f:
        l.append(int(line))

for mass in l:
    while mass > 0:
        mass = geerten(mass)
        total = total + max(0, mass)
        # print(mass)

print(total)
