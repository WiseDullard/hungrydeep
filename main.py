import textwrap
import time
from story.intro import intro
from entities.player import player

def stylized_print(text):
    if len(text) < 80:
        print(text)
    else:
        wrapped_text = textwrap.wrap(text, width= 60)
        for line in wrapped_text:
            print(line)
            time.sleep(1.5)


def main():
    stylized_print(intro)
    while True:
        command = input("/n> ").lower().strip()
        if command == "quit":
            print("Thanks for playing!")
            break

        words = command.split()
        if len(words) > 0:
            verb = words[0]
        if len(words) > 1:
            noun = words[1]
        elif len(words) >= 3:
            print("Commands must be two words long.")
        else:
            print("No command detected.")

        if verb in ["move", "go", "travel", "walk"]:
            if noun in ["north", "east", "south", "west"]:
                player.move(noun)
            else:
                player.use_stairs(noun)
        

main()