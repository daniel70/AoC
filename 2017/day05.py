with open("input05.txt") as f:
    instructions = [int(line.strip()) for line in f]

counter = 0
pointer = 0
while 0 <= pointer < len(instructions):
    moves = instructions[pointer]
    instructions[pointer] += 1
    pointer = pointer + moves
    counter += 1

print("answer 1:", counter)
