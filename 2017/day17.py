spinlocks = [0]
steps = 349
pos = 0
for i in range(1, 2018):
    pos = (pos + steps) % i + 1
    spinlocks.insert(pos, i)

print("answer 1:", spinlocks[spinlocks.index(2017) + 1])

spinlocks = [0]
pos = after_zero = 0
for i in range(1, 50_000_000):
    if (pos + steps) % i == 0:
        after_zero = i
    pos = (pos + steps) % i + 1

print("answer 2:", after_zero)
