import re


row, column = [int(x) for x in re.findall(r"\d+", open("input25.txt").readline())]
base = (column * (column + 1)) // 2

# every row step we increase, starting at column, with one
for i in range(column, column + row - 1):
    base += i

code = 20151125
for _ in range(base - 1):
    code = code * 252533 % 33554393

print("answer 1:", code)
print("answer 2: not needed")
