"""
Advent of Code 2019, day 7, puzzle 1
"""
with open("input07.txt") as f:
    line = f.readline()
from itertools import permutations
# line = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
# line = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
# line = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
codes = [int(s) for s in line.split(",")]


def intcode(inputs):
    iinputs = iter(inputs)
    counter = 0
    while True:
        opcode = codes[counter]
        if opcode == 99:
            return

        op = opcode % 100
        C = opcode // 100 % 10
        p1 = codes[counter + 1] if C else codes[codes[counter + 1]]
        if op not in [3, 4]:  # input and output don't have a 2nd parameter
            B = opcode // 1000 % 10
            p2 = codes[counter + 2] if B else codes[codes[counter + 2]]
            A = opcode // 10000 % 10

        # print(opcode, op, C)
        if op == 1:  # sum
            codes[codes[counter + 3]] = p1 + p2
            counter += 4

        elif op == 2:  # product
            codes[codes[counter + 3]] = p1 * p2
            counter += 4

        elif op == 3:
            input = next(iinputs)
            if C == 0:
                codes[codes[counter + 1]] = input
            elif C == 1:
                codes[counter + 1] = input
            counter += 2

        elif op == 4:
            # print(f"Test Output: {p1}.")
            counter += 2
            return p1

        elif op == 5:  # jump if true
            if p1 != 0:
                counter = p2
            else:
                counter += 3

        elif op == 6:  # jump if false
            if p1 == 0:
                counter = p2
            else:
                counter += 3

        elif op == 7:  # less than
            if p1 < p2:
                codes[codes[counter + 3]] = 1
            else:
                codes[codes[counter + 3]] = 0
            counter += 4

        elif op == 8:  # equals
            if p1 == p2:
                codes[codes[counter + 3]] = 1
            else:
                codes[codes[counter + 3]] = 0
            counter += 4

        else:
            print(f"invalid opcode {opcode} at {counter}")
            break

A = intcode
B = intcode
C = intcode
D = intcode
E = intcode
highest_output = 0
highest_phase = []
phases = permutations([0, 1, 2, 3, 4], 5)
for phase in phases:
    iphase = iter(phase)
    a = A([next(iphase), 0])
    b = B([next(iphase), a])
    c = C([next(iphase), b])
    d = D([next(iphase), c])
    e = E([next(iphase), d])
    # print(f'phase {phase} = {e}')
    if e > highest_output:
        highest_output = e
        highest_phase = phase

print(f'phase {highest_phase} has output {highest_output}')
