garden = { i+j*1j:c for i, r in enumerate(open(r"2024\input12.txt").readlines())
                    for j, c in enumerate(r.strip())}

def walk(pos, plant, region):
    if pos in seen or garden[pos] != plant:
        return
    
    region.append(pos)
    seen.add(pos)
    
    # call the neighbours
    for neighbour in [pos + dir for dir in [-1, 1, -1j, 1j]]:
        if neighbour in garden and garden[neighbour] == plant:
            walk(neighbour, plant, region)


seen, regions = set(), list()
for k, v in garden.items():
    if k not in seen:
        regions.append([])
        walk(k, v, regions[-1])

answer1 = 0
answer2 = 0
for region in regions:
    for pos in region:
        # top
        if pos-1 not in region:
            answer1 += len(region)
            if pos-1j not in region or pos-1-1j in region:
                answer2 += len(region)
        # bottom
        if pos+1 not in region:
            answer1 += len(region)
            if pos-1j not in region or pos+1-1j in region:
                answer2 += len(region)
        # left
        if pos-1j not in region:
            answer1 += len(region)
            if pos-1 not in region or pos-1-1j in region:
                answer2 += len(region)
        # right
        if pos+1j not in region:
            answer1 += len(region)
            if pos-1 not in region or pos-1+1j in region:
                answer2 += len(region)

print(answer1)
print(answer2)
