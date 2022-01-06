def possible(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 1
    return 0


total1 = 0
total2 = 0
values = []
with open("input03.txt") as f:
    for line in f:
        line = line.rstrip()
        values.extend(list(map(int, line.split())))

for i in range(len(values) // 9):
    window = values[i * 9:i * 9 + 9]
    total1 += possible(window[0], window[1], window[2])
    total1 += possible(window[3], window[4], window[5])
    total1 += possible(window[6], window[7], window[8])
    total2 += possible(window[0], window[3], window[6])
    total2 += possible(window[1], window[4], window[7])
    total2 += possible(window[2], window[5], window[8])

print("answer 1:", total1)
print("answer 2:", total2)
