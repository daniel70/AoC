from collections import namedtuple, Counter
import re

numbers = re.compile(r"-?\d+")
Particle = namedtuple("Particle", "px py pz vx vy vz ax ay az Σv Σa nr", defaults=(0, 0, 0))
instructions = []
with open("input20.txt") as f:
    for idx, line in enumerate(f):
        line = line.strip()
        p = Particle(*[int(x) for x in numbers.findall(line)])
        p = p._replace(Σv=abs(p.vx) + abs(p.vy) + abs(p.vz))
        p = p._replace(Σa=abs(p.ax) + abs(p.ay) + abs(p.az))
        p = p._replace(nr=idx)
        instructions.append(p)

# the particle that stays closest to origin is the one with the lowest acceleration
# in case of a tie, the winner is the particle with the lowest velocity
# so, we sort first on the sum of velocities then on the sum of accelerations
instructions.sort(key=lambda p: p.Σv)
instructions.sort(key=lambda p: p.Σa)
print("answer 1:", instructions[0].nr)

for step in range(100):
    p: Particle
    c = Counter([(p.px, p.py, p.pz) for p in instructions])
    doubles = [p for p, count in c.items() if count > 1]
    for double in doubles:
        instructions = [
            p for p in instructions if not (p.px == double[0] and p.py == double[1] and p.pz == double[2])
        ]

    for idx, p in enumerate(instructions):
        p = p._replace(vx=p.vx + p.ax, vy=p.vy + p.ay, vz=p.vz + p.az)
        p = p._replace(px=p.px + p.vx, py=p.py + p.vy, pz=p.pz + p.vz)
        instructions[idx] = p

print("answer 2:", len(instructions))
