import random
import time

from entities import player
from combat import battle_logic

player_character = player.player

def start_battle():
    enemies = []
    enemies += player_character.location.entities
    turn_counter = 0
    print("--- Defend Yourself ---")
    while player_character.is_alive:
        turn_counter += 1

        #Player Turn
        choice = input("Your Move /n> ").lower()
        if choice in ["run", "flee", "retreat"]:
            n = random.randint(1, 10)
            if n <= 5:
                battle_logic.run_away(player_character)
                break
            else:
                print("You cannot get away.")
                time.sleep(1.5)

        elif choice in ["attack", "damage", "strike"]:
            damage = battle_logic.attack(player_character, enemies[0])
            enemies[0].health -= damage
            print(f"You deal {damage} damage.")

        elif choice in ["wait", "pass", "nothing"]:
            print("You do nothing")
            time.sleep(1.5)

        else:
            print("Not a valid command.")
            time.sleep(1.5)

        if enemies[0].health <= 0:
            print(f"You slay the {enemies[0].name}")
            enemies.remove(enemies[0])

        if len(enemies) == 0:
            print("You won")
            break

        #Enemy turn
        for enemy in enemies:
            print(f"{enemy.name} attacks.")
            damage = battle_logic.attack(enemy, player_character)
            player_character.health -= damage
            time.sleep(1.5)
            print(f"{enemy.name} deals {damage} damage.")
            time.sleep(1.5)
            

            if player_character.health <= 0:
                print(f"{enemy.name} slays you.")
                return player.game_over()
            else:
                print(f"You have {player_character.health} health left.")
                time.sleep(1.5)


