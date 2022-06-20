import re
from dataclasses import dataclass
from itertools import product, combinations, chain
from pprint import pprint
from copy import copy

@dataclass
class Character:
    hp: int
    damage: int
    armor: int


@dataclass()
class Item:
    name: str
    cost: int
    damage: int
    armor: int


weapons = (
    Item("dagger", 8, 4, 0),
    Item("shortsword", 10, 5, 0),
    Item("warhammer", 25, 6, 0),
    Item("longsword", 40, 7, 0),
    Item("greataxe", 74, 8, 0),
)

armor = (
    None,
    Item("leather", 13, 0, 1),
    Item("chainmail", 31, 0, 2),
    Item("splintmail", 53, 0, 3),
    Item("bandedmail", 75, 0, 4),
    Item("platemail", 102, 0, 5),
)

rings = (
    None,
    None,
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
)


def fight(player: Character, boss: Character) -> bool:
    while True:
        boss.hp -= max(player.damage - boss.armor, 1)
        if boss.hp <= 0:
            return True

        player.hp -= max(boss.damage - player.armor, 1)
        if player.hp <= 0:
            return False


boss = Character(*[int(s) for s in re.findall(r"\d+", open("input21.txt").read())])
cheapest = None
expensive = None
for items in product(weapons, armor, list(combinations(rings, 2))):
    # flatten and remote Nones
    items = [i for i in [items[0], items[1], *items[2]] if i is not None]
    player = Character(
        100,
        sum([x.damage for x in items]),
        sum([x.armor for x in items])
    )
    cost = sum([x.cost for x in items])
    if fight(player, copy(boss)):
        if cheapest is None or cost < cheapest:
            cheapest = cost
    else:
        if expensive is None or cost >= expensive:
            expensive = cost

print("Answer 1:", cheapest)
print("Answer 2:", expensive)
