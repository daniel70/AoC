instructions = open("input04.txt").readlines()
one = two = 0
for line in instructions:
    line = line.strip()
    if len(line.split()) == len(set(line.split())):
        one += 1

    sorted_passwords = ["".join(sorted(password)) for password in line.split()]
    if len(sorted_passwords) == len(set(sorted_passwords)):
        two += 1

print("answer 1:", one)
print("answer 1:", two)
