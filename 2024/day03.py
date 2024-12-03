import re
mul = re.compile(r"(don\'t|mul\((\d{1,3}),(\d{1,3})\)|do)")
answer1 = answer2 = 0
data = open(r".\2024\input03.txt").read().strip().split("\n")
do = True
for line in data:
    matches = mul.findall(line)
    for match in matches:
        instruction, left, right = match
        if instruction == "do":
            do = True
        elif instruction == "don't":
            do = False
        else:
            temp = (int(left) * int(right))
            answer1 += temp
            answer2 += temp if do else 0


print("answer 1: ", answer1)
print("answer 2: ", answer2)