ids = []
with open('input02.txt') as f:
    for line in f:
        for s in ids:
            c: int = 0
            for a, b in zip(line, s):
                if a != b:
                    c += 1
                if c > 1:
                    break

            if c == 1:
                # found it
                code = []
                for a, b in zip(line, s):
                    if a == b:
                        code.append(a)
                print(''.join(code))

        ids.append(line)
