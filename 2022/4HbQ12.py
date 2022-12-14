grid = open('test12.txt').read().replace('\n', '')
coords = lambda i: complex(*divmod(i, 8))
height = lambda c: ord(grid.get(c, 'Z').replace('S', 'a'))
source = coords(grid.index('E'))
grid = {coords(x): grid[x] for x in range(len(grid))}

for target in 'S', 'Sa':
    todo, done = [(source, 0)], {source}

    while todo:
        old, dist = todo.pop(0)
        if grid[old] in target:
            print(dist)
            break

        for new in (old+1, old-1, old+1j, old-1j):
            if new not in done and height(old) - height(new) <= 1:
                todo.append((new, dist+1))
                done.add(new)
