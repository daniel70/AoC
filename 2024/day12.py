garden = { i+j*1j:c for i, r in enumerate(open(r"2024\input12.txt").readlines())
                    for j, c in enumerate(r.strip())}
seen = {}

def walk(pos, plant, region):
    if pos in seen or garden[pos] != plant:
        return
    
    region.append(pos)
    
    # how many sides do I have?
    sides = 4
    for neighbour in [pos + dir for dir in [-1, 1, -1j, 1j]]:
        if neighbour in garden and garden[neighbour] == plant:
            sides -= 1
        seen[pos] = sides
    
    # call the neighbours
    for neighbour in [pos + dir for dir in [-1, 1, -1j, 1j]]:
        if neighbour in garden and garden[neighbour] == plant:
            walk(neighbour, plant, region)


regions = []
for k, v in garden.items():
    if k not in seen:
        regions.append([])
        walk(k, v, regions[-1])

answer1 = []
for region in regions:
    parameter = 0
    for pos in region:
        parameter += seen[pos]
    answer1.append(parameter * len(region))

answer2 = []
for region in regions:
    parameter = 0
    for pos in region:
        # top
        if pos-1 not in region:
            if pos-1j not in region or pos-1-1j in region:
                parameter += 1
        # bottom
        if pos+1 not in region:
            if pos-1j not in region or pos+1-1j in region:
                parameter += 1
        # left
        if pos-1j not in region:
            if pos-1 not in region or pos-1-1j in region:
                parameter += 1
        # right
        if pos+1j not in region:
            if pos-1 not in region or pos-1+1j in region:
                parameter += 1
    answer2.append(parameter * len(region))


print(sum(answer1))
print(sum(answer2))
