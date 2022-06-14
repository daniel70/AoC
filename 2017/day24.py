bricks = []
with open("input24.txt") as f:
    for line in f:
        line = line.strip()
        l, r = line.split("/")
        bricks.append((int(l), int(r)))


def bridges(bricks, bridge=(), pins: int = 0):
    for brick in bricks:
        if pins in brick:
            new_bridge = bridge + brick
            new_bricks = bricks.copy()
            new_bricks.remove(brick)
            yield from bridges(new_bricks, new_bridge, pins=brick[abs(brick.index(pins) - 1)])
    else:
        # there are no more bricks to add to the bridge, yield the bridge
        yield bridge


solutions = list(bridges(bricks))
print("answer 1:", max(sum(bridge) for bridge in solutions))
longest = max(len(bridge) for bridge in solutions)
print("answer 2:", max(sum(bridge) for bridge in solutions if len(bridge) == longest))
