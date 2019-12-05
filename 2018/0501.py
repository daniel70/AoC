import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
combinations = [lc+uc for lc, uc in zip(lowercase, uppercase)] + [uc+lc for lc, uc in zip(lowercase, uppercase)]
line = 'dabAcCaCBAcCcaDA'
with open("input05.txt") as f:
    line = f.readline()

match = True
while match:
    for c in combinations:
        match = False
        if c in line:
            match = True
            line = line.replace(c, '', 1)
            # print(f'replacing {c}, line is {line}')
            break

print(f"resulting line is {len(line)-1} units")