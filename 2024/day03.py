import re
mul = re.compile(r"(don\'t|do|mul\((\d{1,3}),(\d{1,3})\))")
answer1 = answer2 = 0
data = open(r"input03.txt").read().strip().split("\n")
do = True
for line in data:
    for finding in mul.findall(line):
        match finding:
            case "do", _, _:
                do = True
            case "don't", _, _:
                do = False
            case _, left, right:
                temp = (int(left) * int(right))
                answer1 += temp
                answer2 += temp if do else 0

print("answer 1: ", answer1)
print("answer 2: ", answer2)
