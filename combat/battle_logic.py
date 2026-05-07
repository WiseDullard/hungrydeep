from entities import player

def attack(attacker, target):
    if attacker == player.player:
        if player.player.weapon == None:
            hp_damage = 5 - target.defence
            
        else:
            hp_damage = player.player.weapon.damage - target.defence

    else:
        hp_damage = attacker.damage - target.defence
    if hp_damage < 0:
        hp_damage = 0
    return hp_damage

def run_away(player):
    print("You flee the battle.")
    player.location = player.previous_room
    player.health = 100

