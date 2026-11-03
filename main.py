from story import story_functions, story_text
from entities import player, monster, items
from combat import battle_manager


def main():
    
    story_functions.story_print(story_text.intro)
    story_functions.story_print("------ The Hungry Deep ------")
    print("Type help for instructions.")
    while True:
        n = 0
        for item in player.player.inventory:
            if item.name == "lantern":
                lantern = player.player.inventory[n]
            else:
                n += 1

        if len(player.player.location.entities) >= 1:
            if isinstance(player.player.location.entities[0], monster.hollow_giant):
                if lantern.is_lit == True:
                    battle_manager.hollow_giant_battle()
            elif isinstance(player.player.location.entities[0], monster.ghost):
                battle_manager.ghost_battle()
            else:
                battle_manager.start_battle()

        if player.player.location.name.lower() == "heart chamber-by the heart":
            story_functions.story_print(player.player.location.items[0].description)
            story_functions.final_choice()

        command = input("/n> ").lower().strip()
        if command in ["quit", "exit"]:
            print("Thanks for playing!")
            break

        if command == "help":
            story_functions.help()
            continue

        words = command.split()
        if len(words) > 0:
            verb = words[0]
        if len(words) > 1:
            noun = words[1]
        elif len(words) >= 3:
            print("Commands cannot be more than two words long.")
        else:
            print("No valid command detected.")

        if verb in ["move", "go", "travel", "walk"]:
            if noun in ["north", "east", "south", "west"]:
                player.move(noun)
            elif noun in ["up", "down"]:
                player.use_stairs(noun)
            else:
                print("No valid direction detected.")
                continue
            continue
        
        if verb in ["inspect", "examine", "look", "study"]:
            if len(words) > 1:
                player.inspect(noun)
            else:
                player.inspect("room")
            continue

        if verb in ["get", "aquire", "gather"]:
            if len(words) > 1:
                player.get(noun)
            else:
                print("Command must have target.")
            continue

        if verb in ["equip", "wear"]:
            if len(words) > 1:
                player.equip(noun)
            else:
                print("Command must have target.")
            continue

        if verb == "use":
            if len(words) > 1:
                player.use_item(noun)
            else:
                print("Command must have target.")
            continue

        #elif verb == "stab":
            #if noun == "heart":
                #if player.player.location.name.lower == "heart chamber-by the heart":
                    #story_functions.stab_heart()

main()