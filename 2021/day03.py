lines = []
with open('input03.txt') as f:
    for line in f:
        lines.append(line.rstrip())

tie = len(lines) // 2
bits = len(lines[0])
Σγ = Σε = ""
for bit in range(bits):
    ones = 0
    for nr in lines:
        ones += int(nr[bit])

    Σγ += str(int(ones >= tie))
    Σε += str(int(ones < tie))

power = int(Σγ, 2) * int(Σε, 2)
print('answer 1:', power)

oxy = co2 = ""
oxy_lines = lines[:]
for bit in range(bits):
    ones = 0
    for nr in oxy_lines:
        ones += int(nr[bit])

    oxy += str(int(ones >= (len(oxy_lines) / 2)))
    oxy_lines = [l for l in oxy_lines if l[bit] == oxy[bit]]

    if len(oxy_lines) == 1:
        oxy = oxy_lines[0]
        break

co2_lines = lines[:]
for bit in range(bits):
    ones = 0
    for nr in co2_lines:
        ones += int(nr[bit])

    co2 += str(int(ones < (len(co2_lines) / 2)))
    co2_lines = [l for l in co2_lines if l[bit] == co2[bit]]

    if len(co2_lines) == 1:
        co2 = co2_lines[0]
        break

power = int(oxy, 2) * int(co2, 2)
print('answer 2:', power)
