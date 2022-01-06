keypad1 = [
    ["0", "0", "0", "0", "0"],
    ["0", "1", "2", "3", "0"],
    ["0", "4", "5", "6", "0"],
    ["0", "7", "8", "9", "0"],
    ["0", "0", "0", "0", "0"],
]

keypad2 = [
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "2", "3", "4", "0", "0"],
    ["0", "5", "6", "7", "8", "9", "0"],
    ["0", "0", "A", "B", "C", "0", "0"],
    ["0", "0", "0", "D", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0"],
]


def change_key(button, direction, keypad):
    if direction == "U":
        new_location = [button[0] - 1, button[1]]
    if direction == "D":
        new_location = [button[0] + 1, button[1]]
    if direction == "L":
        new_location = [button[0], button[1] - 1]
    if direction == "R":
        new_location = [button[0], button[1] + 1]
    if keypad[new_location[0]][new_location[1]] == "0":
        return button
    return new_location


button1 = [2, 2]  # button 5
button2 = [3, 1]  # button 5
answer1 = ""
answer2 = ""
with open("input02.txt") as f:
    for line in f:
        line = line.strip()
        for c in line:
            button1 = change_key(button1, c, keypad1)
            button2 = change_key(button2, c, keypad2)

        answer1 += keypad1[button1[0]][button1[1]]
        answer2 += keypad2[button2[0]][button2[1]]

print("answer 1:", answer1)
print("answer 2:", answer2)
