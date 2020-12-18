answer1 = answer2 = 0
with open("input02.txt") as f:
    for line in f:
        line = line.strip()
        l, w, h = line.split('x')
        l = int(l); w = int(w); h = int(h)
        answer1 += (2 * l * w) + (2 * w * h) + (2 * h * l)
        s = sorted([l, w, h])
        s1, s2 = s[:2]
        answer1 += s1 * s2
        answer2 += 2*s1 + 2*s2
        answer2 += l*w*h

print(answer1)
print(answer2)