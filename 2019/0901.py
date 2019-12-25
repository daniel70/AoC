"""
Advent of Code 2019, day 9, puzzle 1
Use a generator to solve this puzzle
"""
from itertools import permutations

debug = False
with open("input07.txt") as f:
    line = f.readline()

line = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
# line = "1102,34915192,34915192,7,4,7,99,0"
codes = [int(s) for s in line.split(",")]

init = 1
counter = 0
opcode = 0
relative_base = 0

while True:
    print(f'{counter=} {relative_base=}')
    opcode = codes[counter]
    if opcode == 99:
        print('stop')

    op = opcode % 100

    C = opcode // 100 % 10  # param 1
    if C == 0: # position mode
        p1 = codes[codes[counter + 1]]
    elif C == 1:  # immediate mode
        p1 = codes[counter + 1]
    elif C == 2:  # relative mode
        p1 = codes[relative_base + codes[counter + 1]]

    if op not in [3, 4, 9]:  # input and output don't have a 2nd parameter
        B = opcode // 1000 % 10  # param 2
        if B == 0:  # position mode
            p2 = codes[codes[counter + 2]]
        elif B == 1:  # immediate mode
            p2 = codes[counter + 2]
        elif B == 2:  # relative mode
            p2 = codes[relative_base + codes[counter + 2]]

        A = opcode // 10000 % 10

    if op == 1:  # sum
        codes[codes[counter + 3]] = p1 + p2
        counter += 4

    elif op == 2:  # product
        codes[codes[counter + 3]] = p1 * p2
        counter += 4

    elif op == 3:  # input
        # signal = yield
        if C == 0:
            codes[codes[counter + 1]] = init
        elif C == 1:
            codes[counter + 1] = init
        counter += 2

    elif op == 4:
        # print(f"Test Output: {p1}.")
        counter += 2
        print(f'Output: {p1} ({relative_base=})')

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

    elif op == 9:  # relative base
        relative_base += p1
        counter += 2

    else:
        print(f"invalid opcode {opcode} at {counter}")
        break



