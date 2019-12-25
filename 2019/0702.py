"""
Advent of Code 2019, day 7, puzzle 2
Use a generator to solve this puzzle
"""
from itertools import permutations

debug = False
with open("input07.txt") as f:
    line = f.readline()

input_codes = [int(s) for s in line.split(",")]


def intcode():
    codes = input_codes[:]
    counter = 0
    while True:
        opcode = codes[counter]
        if opcode == 99:
            return StopIteration

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

        elif op == 3:  # input
            signal = yield
            if C == 0:
                codes[codes[counter + 1]] = signal
            elif C == 1:
                codes[counter + 1] = signal
            counter += 2

        elif op == 4:
            # print(f"Test Output: {p1}.")
            counter += 2
            yield p1

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


highest_output = 0
highest_phase = None
for phase in permutations([5, 6, 7, 8, 9], 5):
    signal = 0
    amps = [intcode(), intcode(), intcode(), intcode(), intcode()]

    # phase initialization
    for i, amp in enumerate(amps):
        next(amp)
        amp.send(phase[i])

    # feedback loop
    try:
        while True:
            for amp in amps:
                signal = amp.send(signal)

            if signal > highest_output:
                highest_output = signal
                highest_phase = phase

            for amp in amps:
                next(amp)

    except StopIteration:
        pass

print(f'phase {highest_phase} has output {highest_output}')
