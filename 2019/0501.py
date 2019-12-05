"""
Advent of Code 2019, day 5, puzzle 1
"""
with open("input05.txt") as f:
    line = f.readline()

codes = [int(s) for s in line.split(",")]
counter = 0
while True:
    opcode = codes[counter]
    op = opcode % 100
    C = opcode // 100 % 10
    B = opcode // 1000 % 10
    A = opcode // 10000 % 10
    if opcode == 99:
        break

    elif op == 3:
        input = int(input("Enter ID #"))
        if C == 0:
            codes[codes[counter + 1]] = input
        elif C == 1:
            codes[counter + 1] = input
        counter += 2

    elif op == 4:
        if C == 0:
            print(f"Test Output: {codes[codes[counter + 1]]}")
        elif C == 1:
            print(f"Test Output: {codes[counter + 1]}")
        counter += 2

    elif op in [1, 2]:  # sum or product
        if C == 0:  # position
            p1 = codes[codes[counter + 1]]
        elif C == 1:  # immediate
            p1 = codes[counter + 1]
        else:
            print(f"invalid p1: {opcode} at {counter}")

        if B == 0:  # position
            p2 = codes[codes[counter + 2]]
        elif B == 1:  # immediate
            p2 = codes[counter + 2]
        else:
            print(f"invalid p2: {opcode} at {counter}")

        if opcode % 100 == 1:
            codes[codes[counter + 3]] = p1 + p2
        elif opcode % 100 == 2:
            codes[codes[counter + 3]] = p1 * p2

        counter += 4

    else:
        print(f"invalid opcode {opcode} at {counter}")
        break
