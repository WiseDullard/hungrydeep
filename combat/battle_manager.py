import random
import time

from entities import player
from combat import battle_logic
from story import story_functions

player_character = player.player
sleep = time.sleep

def start_battle():
    enemies = []
    enemies += player_character.location.entities
    turn_counter = 0
    print("--- Defend Yourself ---")
    while player_character.is_alive:
        turn_counter += 1

        #Player Turn
        sleep(1)
        print(f"Turn {turn_counter}.")
        sleep(1)
        choice = input("Your Move /n> ").lower()
        if choice in ["run", "flee", "retreat"]:
            n = random.randint(1, 10)
            if n <= 5:
                battle_logic.run_away(player_character)
                break
            else:
                print("You cannot get away.")
                sleep(1)
                
        elif choice in ["attack", "damage", "strike"]:
            damage = battle_logic.attack(player_character, enemies[0])
            enemies[0].health -= damage
            print(f"You deal {damage} damage.")
            sleep(1)
            
        elif choice in ["wait", "pass", "nothing"]:
            print("You do nothing")
            sleep(1)
            

        else:
            print("Not a valid command.")
            sleep(1)
            

        if enemies[0].health <= 0:
            print(f"You slay the {enemies[0].name}")
            sleep(1)
            player_character.location.entities.remove(enemies[0])
            enemies.remove(enemies[0])
            

        if len(enemies) == 0:
            player_character.health = 100
            print("You won!")
            sleep(1)
            break

        #Enemy turn
        for enemy in enemies:
            print(f"{enemy.name} attacks.")
            damage = battle_logic.attack(enemy, player_character)
            player_character.health -= damage
            sleep(1)
            print(f"{enemy.name} deals {damage} damage.")
            sleep(1)
            

            if player_character.health <= 0:
                print(f"{enemy.name} slays you.")
                sleep(1)
                return player.game_over()
            else:
                print(f"You have {player_character.health} health left.")
                sleep(1)
                

def ghost_battle():
    enemies = []
    enemies += player_character.location.entities
    turn_counter = 0
    story_functions.story_print("As you approach the brazier in the centre of the room, three ghostly figures emerge from the walls to your north east and west. They bear ragged and dessicated features, their mouths move soundlessly as if trying to speak words you cannot comprehend. They begin to drift towards you. ")
    print("--- Defend Yourself ---")
    while player_character.is_alive:
        turn_counter += 1
        if len(player_character.location.entities) == 0:
            enemies = []
        if len(enemies) == 0:
            print("You Survived!")
            sleep(1)
            story_functions.story_print("The smoke from the feather-root hangs heavily in the air while you try to still your shaking hands. After a moment you notice the smoke seems to be slowly drifting towards the north wall.")
            break

        # Player Turn
        print(f"Turn {turn_counter}.")

        command = input("Your Move /n> ").lower().strip()
        words = command.split()
        if len(words) > 0:
            verb = words[0]
        if len(words) > 1:
            noun = words[1]
        elif len(words) >= 3:
            print("Commands cannot be more than two words long.")
            sleep(1)
        #else:
            #print("No valid command detected.")
            

        if verb in ["attack", "damage", "strike"]:
            damage = battle_logic.attack(player_character, enemies[0])
            print(f"Your {player_character.weapon.name} passes through the ghost.")
            sleep(1)

        elif verb in ["wait", "pass", "nothing"]:
            print("You do Nothing")
            sleep(1)

        elif verb in ["use", "burn"]:
            i = 0
            for item in player_character.inventory:
                if noun == "feather-root":
                    if item.name == "feather-root":
                        story_functions.story_print("You throw the feather-root into the brazier and light it with your flint and steel.")
                        player_character.inventory.remove(player_character.inventory[i])
                        player_character.location.items[1].is_lit = True
                        sleep(1)
                else:
                    i += 1
                    
        
        else:
            print("Not a valid command.")
            sleep(1)
            

        # Enemy Turn
        for enemy in enemies:
            if player_character.location.items[1].is_lit == True:
                story_functions.story_print(f"{enemy.name} recoils at the smoke and cries out in silent horror, it flees through the nearest wall.")
                sleep(1)
                player_character.location.entities.remove(enemy)
                #enemies.remove(enemies[0])
                

            elif enemy.distance > 0:
                print(f"{enemy.name} drifts closer.")
                sleep(1)
                enemy.distance -= 1
                

            else:
                sleep(1)
                print(f"{enemy.name} attacks.")
                damage = battle_logic.attack(enemy, player_character)
                player_character.health -= damage
                sleep(1)
                print(f"{enemy.name} deals {damage} damage.")
                sleep(1)
                print(f"you have {player_character.health} health left.")
                sleep(1)
                return
                

            if len(enemies) == 0:
                print("The Ghosts have fled.")
                player_character.health = 100
                sleep(1)
                story_functions.story_print("As you catch your breath you notice the smoke drifting slowly towards the wall opposite the door you entered from. Upon closer inspection, you notice it is passing through the gaps between the bricks in the wall.")
                
            
            if player_character.health <= 0:
                print(f"{enemy.name} slays you.")
                return player.game_over()
            
            


def hollow_giant_battle():
    n = 0
    dodge_counter = 3
    for item in player_character.inventory:
        if item.name == "lantern":
            lantern = player_character.inventory[n]
        else:
            n += 1
    enemies = []
    enemies += player_character.location.entities
    turn_counter = 0
    print("--- Defend Yourself ---")
    while player_character.is_alive:
        turn_counter += 1

        # Player Turn
        print(f"Turn {turn_counter}.")
        if lantern.is_lit == False:
            story_functions.story_print("In the darkness you hear nothing, after a few moments you realize that the Giant has stopped moving, and you see a dull red glow, pulsing at the southern end of the massive chamber.")
            break

        command = input("Your Move /n> ").lower().strip()
        words = command.split()
        if len(words) > 0:
            verb = words[0]
        if len(words) > 1:
            noun = words[1]
        elif len(words) >= 3:
            print("Commands cannot be more than two words long.")
            sleep(1)
        #else:
            #print("No valid command detected.")
            #sleep
            

        if verb in ["attack", "damage", "strike"]:
            damage = battle_logic.attack(player_character, enemies[0])
            print(f"Your {player_character.weapon.name} bounces harmlessly off the flesh of the Giant.")
            sleep(1)

        elif verb in ["wait", "pass", "nothing"]:
            print("You do Nothing")
            sleep(1)

        elif verb in ["douse", "extinguish"]:
            if noun == "lantern":
                lantern.is_lit = False
                print("You douse the light of your lantern.")
                sleep(1)
        
        else:
            print("Not a valid command.")
            sleep(1)

        # Enemy Turn
        for enemy in enemies:
            if lantern.is_lit == False:
                print("You hold your breath in anticipation of a blow that does not come.")
                sleep(1)
            
            else:
                n = random.randint(1, 10)
                print(f"{enemy.name} attacks.")
                sleep(1)
            
                if n >= 7:
                    damage = battle_logic.attack(enemy, player_character)
                    player_character.health -= damage
                    print(f"{enemy.name} deals {damage} damage.")
                    sleep(1)
                else:
                    print("You dive to the side, barely dodging the massive fist of the Giant.")
                    dodge_counter -= 1
                    sleep(1)
            
                if dodge_counter == 0:
                    story_functions.story_print("As the Giant strikes the floor where you stood, your lantern is thrown from your belt, it clatters to the floor and goes out.")
                    lantern.is_lit = False
                    sleep(1)
            
                if player_character.health <= 0:
                    print(f"{enemy.name} slays you.")
                    sleep(1)
                    return player.game_over()
                else:
                    print(f"You have {player_character.health} health left.")
                    sleep(1)