from story import intro, story_functions
from entities import player


def main():
    story_functions.story_print(intro.fast_test)
    while True:
        command = input("/n> ").lower().strip()
        if command in ["quit", "exit"]:
            print("Thanks for playing!")
            break

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
        

main()