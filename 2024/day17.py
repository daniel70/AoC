
def test(program, registers=None, both=True):
    global A, B, C, pointer, output
    pointer = 0
    output = []
    if registers is not None:
        A, B, C = registers
    while pointer < len(program):
        pointer = computer(program[pointer], program[pointer + 1])

    if both:
        return output, [A, B, C]
    else:
        return output

def combo(operant: int) -> int:
    return [0, 1, 2, 3, A, B, C][operant]


def computer(opcode: int, operant: int):
    global A, B, C, pointer, output
    match opcode:
        case 0: A = A // (2 ** combo(operant))
        case 1: B = B ^ operant
        case 2: B = combo(operant) % 8
        case 3: pointer = operant - 2 if A != 0 else pointer
        case 4: B = B ^ C
        case 5: output.append(combo(operant) % 8)
        case 6: B = A // (2 ** combo(operant))
        case 7: C = A // (2 ** combo(operant))
    return pointer + 2


lines = [line for line in open("input17.txt").read().splitlines() if line]
A = int(lines[0].split(":")[1])
B = int(lines[1].split(":")[1])
C = int(lines[2].split(":")[1])
program = list(map(int, lines[3].split(":")[1].split(",")))
pointer = 0
output = []

answer1 = ",".join([str(c) for c in test(program, [A, B, C], False)])
print(f"answer 1: {answer1}")

"""
Now, for the second part of the answer. I was able to find it by using pen and paper and playing
around with the values. On reddit there was a much better solution by SuperSmurfen here:
https://old.reddit.com/r/adventofcode/comments/1hg38ah/2024_day_17_solutions/m2ggd01/
Z3 is magic and I should learn more about it.

Note that by changing two lines of code in the for loop, the duration went from 2163 seconds to .2 seconds
"""

from z3 import Optimize, BitVec
opt = Optimize()
s = BitVec('s', 64)
a, b, c = s, 0, 0
for x in program:
    b = a % 8 # 2, 4
    b ^= 2 # 1, 2
    # c = a / (1 << b) # 7, 5
    c = a >> b # 7, 5
    b = b ^ c # 4, 5
    # a = a / (1 << 3) # 0, 3
    a >>= 3 # 0, 3
    b ^= 7 # 1, 7
    opt.add((b % 8) == x) # 5, 5
opt.add(a == 0)
opt.minimize(s)
assert str(opt.check()) == 'sat'
print("answer 2:", opt.model().eval(s))
