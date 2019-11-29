tally: int = 0
with open('input01.txt') as f:
    for line in f:
        # print(f'{tally} {line} = {tally+int(line)}')
        tally += int(line)
print(tally)