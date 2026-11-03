import time
import textwrap
from story import story_text

def story_print(text):
    if len(text) < 80:
        print(text)
    else:
        wrapped_text = textwrap.wrap(text, width= 60)
        for line in wrapped_text:
            print(line)
            time.sleep(1.5)

def help():
    command_list = ["use", "move", "inspect", "get"]
    combat_command_list = ["attack", "wait", "use"]
    story_print("Welcome, the following is a list of commands, but first some context about commands. Commands can only consist of two words or less (if an item name is hyphenated, then it requires hyphens when using commands). The commands listed will all work, is will a handful of synonyms for them.")
    time.sleep(1.5)
    for command in command_list:
        print(command)
        time.sleep(1.5)
    story_print("There are also some commands used in combat:")
    time.sleep(1.5)
    for command in combat_command_list:
        print(command)
        time.sleep(1.5)

def final_choice():
    print("Will you listen to the voice (Y/N)?")
    choice = input("/n> ").lower().strip()
    if choice == "y":
        story_print(story_text.vengance_path)
        story_print(story_text.villain_outro)
        story_print("You have chosen to become the Hungry Deep. You go on to torment those who betrayed you for generations. Thanks for Playing!")
        exit()
    elif choice == "n":
        story_print(story_text.forgiveness_path)
        story_print(story_text.hero_outro)
        story_print("You have chosen to sacrifice yourself to end the Hungry Deep. You are a Hero! Thanks for Playing!")
        exit()
    else:
        print("No valid choice detected.")
        final_choice()


def stab_heart():
    story_print(story_text.stab_heart)
    story_print(story_text.outro)
    print("Thanks for playing!")
    exit()
