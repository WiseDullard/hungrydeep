from entities import player
from combat import battle_logic

def start_battle(self):
    enemies = []
    enemies += player.location.entities
    turn_counter = 0
    print("--- Defend Yourself ---")
    while player.is_alive:
        turn_counter += 1

        #Player Turn
        choice = input("Your Move.").lower()
        if choice ==  "attack":
            damage = battle_logic.attack(player.weapon.damage, enemies[0])
            enemies[0].health - damage

        if enemies[0].health <= 0:
            print(f"You slay the {enemies[0].name}")
            enemies.remove(enemies[0])

        if len(enemies) == 0:
            print("You won")
            break


