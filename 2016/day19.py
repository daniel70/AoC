from collections import deque


def take_from_neighbour(elfs):
    q = deque(x for x in range(1, elfs + 1))
    while len(q) > 1:
        q.append(q.popleft())
        q.popleft()

    return q.pop()


def take_from_across(elfs):
    middle = elfs // 2 + 1
    left = deque(x for x in range(1, middle))
    right = deque(x for x in range(elfs + 1, middle, -1))

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]


print("answer 1:", take_from_neighbour(3_017_957))
print("answer 2:", take_from_across(3_017_957))
