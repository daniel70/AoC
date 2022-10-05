from collections import defaultdict
from string import ascii_uppercase as uc
from itertools import count
from dataclasses import dataclass

NR_OF_WORKERS = 5
TIME_BETWEEN_STEPS = 60
steps = defaultdict(list)
uc = '-' + uc  # prepend a char for easy indexing
with open("input07.txt") as f:
    for line in f:
        line = line.strip()
        steps[line[5]].append(line[36])

for final_step in set(item for sublist in steps.values() for item in sublist) - set(steps.keys()):
    steps[final_step] = []


@dataclass
class Worker:
    work: str = ''
    remaining: int = 0


workers: list[Worker] = []
for _ in range(NR_OF_WORKERS):
    workers.append(Worker())


def active_steps(steps, done: set) -> set:
    # determine which tasks can commence based on which have been done
    todo = set()
    for step in steps:
        if done.issuperset({k for k, v in steps.items() if step in v}):
            todo.add(step)
    return todo - done


def generate_steps(steps, todo: set):
    done = set()
    while todo:
        step = sorted(todo)[0]
        done.add(step)
        todo = active_steps(steps, done)
        yield step


def duration() -> int:
    doing = set()
    done = set()
    todo: set = active_steps(steps, done)
    for seconds in count():
        for worker in workers:
            if worker.remaining > 0:
                worker.remaining -= 1
            if worker.remaining == 0 and worker.work:
                # the job is finished
                done.add(worker.work)
                doing.remove(worker.work)
                todo = active_steps(steps, done) - doing
                worker.work = ''

        for worker in workers:
            if not worker.work and todo:
                # assign a step to the worker if available
                worker.work = sorted(todo)[0]
                todo.remove(worker.work)
                doing.add(worker.work)
                worker.remaining = TIME_BETWEEN_STEPS + uc.index(worker.work)

        if not doing:
            break

    return seconds


order = list(generate_steps(steps, active_steps(steps, set())))
print("answer 1:", "".join(order))
print("answer 2:", duration())
