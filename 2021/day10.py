from collections import deque
from statistics import median

points = 0
lines = []
with open('input10.txt') as f:
    for line in f:
        line = line.strip()
        lines.append(line)

close_matches = {"}": "{", "]": "[", ">": "<", ")": "("}
open_matches = {"{": "}", "[": "]", "<": ">", "(": ")"}
syntax_scores = {"}": 1197, "]": 57, ">": 25137, ")": 3}
autocomplete_scores = {"}": 3, "]": 2, ">": 4, ")": 1}

q = deque()
for line in lines[:]:
    for char in line:
        if char in close_matches:
            match = q.pop()
            if close_matches[char] != match:
                # print(f"{line} - Expected \"{open_matches[match]}\" found \"{char}\" ")
                points += syntax_scores[char]
                lines.remove(line)
                break
            continue
        q.append(char)

print('answer 1:', points)

line_scores = []
for line in lines:
    points = 0
    q = deque()
    completion = []
    for char in line:
        if char in close_matches:
            match = q.pop()
            continue
        q.append(char)

    for idx, char in enumerate(reversed(q)):
        completion.append(open_matches[char])
        points *= 5
        points += autocomplete_scores[open_matches[char]]

    # print(f"{line} - Complete by adding {''.join(completion)} - {points}")
    line_scores.append(points)

print('answer 2:', median(line_scores))


