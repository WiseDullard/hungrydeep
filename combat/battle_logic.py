from entities import player

def attack(damage, target):
    hp_damage = target.health - (damage - target.defence)
    if hp_damage < 0:
        hp_damage = 0
    return hp_damage

