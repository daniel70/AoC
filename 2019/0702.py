"""
Advent of Code 2019, day 7, puzzle 1
"""
from itertools import permutations

debug = False
with open("input07.txt") as f:
    line = f.readline()
# line = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"  # 139629729
# line = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10" # 18216
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
highest_phase = []
phases = permutations([5, 6, 7, 8, 9], 5)
# phases = [[9, 8, 7, 6, 5], ]
# phases = [[9, 7, 8, 5, 6], ]

for phase in phases:
    e = 0
    A = intcode()
    B = intcode()
    C = intcode()
    D = intcode()
    E = intcode()
    next(A)
    A.send(phase[0])
    next(B)
    B.send(phase[1])
    next(C)
    C.send(phase[2])
    next(D)
    D.send(phase[3])
    next(E)
    E.send(phase[4])
    try:
        while True:
            a = A.send(e)
            if debug:
                print(f'{a=}')
            b = B.send(a)
            if debug:
                print(f'{b=}')
            c = C.send(b)
            if debug:
                print(f'{c=}')
            d = D.send(c)
            if debug:
                print(f'{d=}')
            e = E.send(d)
            if debug:
                print(f'{e=}')

            if e > highest_output:
                highest_output = e
                highest_phase = phase

            next(A)
            next(B)
            next(C)
            next(D)
            next(E)

    except StopIteration:
        # print(f'{phase=} {e=}')
        pass

print(f'phase {highest_phase} has output {highest_output}')
