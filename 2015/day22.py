from typing import NamedTuple
from dataclasses import dataclass
from copy import copy


@dataclass
class Boss:
    hp: int
    damage: int

    def __str__(self):
        return f"Boss has {self.hp} hit points"

@dataclass
class Wizard:
    hp: int
    armor: int
    mana: int

    def __str__(self):
        return f"Player has {self.hp} hit points, {self.armor} armor, {self.mana} mana"


@dataclass
class Spell:
    name: str
    cost: int
    effect: int
    hp: int
    damage: int
    armor: int
    mana: int

    def __str__(self):
        return self.name


spells = {
    "Magic Missile": Spell(name="Magic Missile", cost=53, effect=0, hp=0, damage=4, armor=0, mana=0),
    "Drain": Spell(name="Drain", cost=73, effect=0, hp=2, damage=2, armor=0, mana=0),
    "Shield": Spell(name="Shield", cost=113, effect=6, hp=0, damage=0, armor=7, mana=0),
    "Poison": Spell(name="Poison", cost=173, effect=6, hp=0, damage=3, armor=0, mana=0),
    "Recharge": Spell(name="Recharge", cost=229, effect=5, hp=0, damage=0, armor=0, mana=101),
}


def cast_spells(wizard, boss, active_spells):
    wizard.armor = 0
    for spell in active_spells:
        print(f"{spell.name} is dealt")
        wizard.hp += spell.hp
        wizard.armor += spell.armor
        wizard.mana += spell.mana
        boss.hp -= spell.damage
        spell.effect -= 1

    return wizard, boss, [spell for spell in active_spells if spell.effect >= 1]


def fight(wizard: Wizard, boss: Boss, mana=0, active_spells: list[Spell] = []) -> int:
    print('\nPlayer Turn')
    print(wizard)
    print(boss)
    wizard, boss, active_spells = cast_spells(wizard, boss, active_spells)
    spell = input(f"Choose from {','.join([spell for spell in spells if spell not in active_spells])}")
    spell = copy(spells[spell])
    print(f"Player casts {spell.name}")
    if spell.effect != 0:
        active_spells.append(copy(spell))
    else: # spell runs immediately
        wizard, boss, _ = cast_spells(wizard, boss, [spell])

    mana += spell.cost
    wizard.mana -= spell.cost
    print(f"active spells are now {active_spells}")

    print('\nBoss turn')
    print(wizard)
    print(boss)
    wizard, boss, active_spells = cast_spells(wizard, boss, active_spells)
    print(f"active spells are now {active_spells}")

    if boss.hp <= 0:
        return mana

    print(f"Boss attacks for {boss.damage} damage.")
    wizard.hp -= max((boss.damage - wizard.armor), 1)

    if wizard.hp <= 0:
        return 0
    else:
        return fight(wizard, boss, mana, active_spells)


boss = Boss(14, 8)
wizard = Wizard(10, 0, 250)
ret = fight(wizard, boss)

# 641 mana is the cheapest yet