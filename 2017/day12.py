pipes = {}
groups = 1
connects = {0}

with open("input12.txt") as f:
    for line in f:
        line.strip()
        l, r = line.split("<->")
        pipes[int(l)] = set([int(x) for x in r.split(', ')])


group_found = True
while group_found:
    pipe_found = True
    while pipe_found:
        pipe_found = False
        for program, via in pipes.items():
            if program in connects:
                if via - connects:
                    pipe_found = True
                    connects |= via
    if groups == 1:
        print("answer 1:", len(connects))

    group_found = False
    for program in pipes.keys():
        if program not in connects:
            connects.add(program)
            groups += 1
            group_found = True
            break

print("answer 2:", groups)
