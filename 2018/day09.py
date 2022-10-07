# I solved this with lists and the second part was very slow, it took 2 hours and 16 minutes.
# I found this beautiful solution on reddit that uses deque
# https://www.reddit.com/r/adventofcode/comments/a4i97s/comment/ebepyc7/?utm_source=share&utm_medium=web2x&context=3
# this takes less than 2 seconds to complete
from collections import deque, defaultdict

with open("input09.txt") as f:
    words = f.readline().split()
    players = int(words[0])
    points = int(words[6])


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


print("answer 1:", play_game(players, points))
print("answer 2:", play_game(players, points * 100))
