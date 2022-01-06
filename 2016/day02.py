def change_button(button, direction):
    if direction == "U" and button > 3:
        return button - 3
    if direction == "D" and button < 7:
        return button + 3
    if direction == "R" and button not in [3, 6, 9]:
        return button + 1
    if direction == "L" and button not in [1, 4, 7]:
        return button - 1
    return button


button = 5
answer = ""
with open("input02.txt") as f:
    for line in f:
        line = line.strip()
        for c in line:
            button = change_button(button, c)
        answer += str(button)

print(answer)
