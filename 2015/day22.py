import re

mana = []


def fight(turn: str, player_hp: int, player_armor: int, player_mana: int, boss_hp: int, effects: dict[str, int], total_mana=0, difficulty="easy"):
    # return early if there is already a better solution
    if mana and total_mana >= min(mana):
        return

    # part two
    if turn == "player" and difficulty == "hard":
        player_hp -= 1

    if player_hp <= 0:
        return

    # run effects
    for effect, turns in effects.items():
        if effect == "Shield":
            if turns == 6:
                player_armor += 7
            if turns == 1:
                player_armor -= 7
        if effect == "Poison":
            boss_hp -= 3
        if effect == "Recharge":
            player_mana += 101

    # decrease and remove effects
    effects = {k: v-1 for k, v in effects.items() if v > 1}

    if boss_hp <= 0:
        mana.append(total_mana)
        return

    if turn == "boss":
        player_hp -= max((boss_damage - player_armor), 1)
        fight("player", player_hp, player_armor, player_mana, boss_hp, effects, total_mana, difficulty)

    elif turn == "player":
        # try all possible attacks
        if player_mana >= 53:
            fight("boss", player_hp, player_armor, player_mana - 53, boss_hp - 4, effects, total_mana + 53, difficulty)
        if player_mana >= 73:
            fight("boss", player_hp + 2, player_armor, player_mana - 73, boss_hp - 2, effects, total_mana + 73, difficulty)
        if player_mana >= 113 and "Shield" not in effects:
            fight("boss", player_hp, player_armor, player_mana - 113, boss_hp, effects | {'Shield': 6}, total_mana + 113, difficulty)
        if player_mana >= 173 and "Poison" not in effects:
            fight("boss", player_hp, player_armor, player_mana - 173, boss_hp, effects | {'Poison': 6}, total_mana + 173, difficulty)
        if player_mana >= 229 and "Recharge" not in effects:
            fight("boss", player_hp, player_armor, player_mana - 229, boss_hp, effects | {'Recharge': 5}, total_mana + 229, difficulty)

    return


boss_hp, boss_damage = [int(s) for s in re.findall(r"\d+", open("input22.txt").read())]
fight("player", 50, 0, 500, boss_hp, {})
print("answer 1:", min(mana))
mana.clear()
fight("player", 50, 0, 500, boss_hp, {}, difficulty="hard")
print("answer 2:", min(mana))
