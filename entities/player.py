from entities.items import dagger, rations
from world.floor_1 import room_list1
from world.floor_2 import room_list2
from world import dungeon_builder
from story import story_functions


class Player(object):
    def __init__(self, location):
        self.location = location
        self.inventory = []
        

player = Player(room_list1[0])
player.inventory += [dagger, rations]

#handle movement
def move(noun):
    if noun in player.location.exits:
        story_functions.story_print(f"You move {noun}")
        player.location = player.location.exits[noun]
        story_functions.story_print(player.location.description)
        
    else:
        story_functions.story_print(f"There is no path {noun}.")

def use_stairs(noun):
    if noun in ["up", "down"]:
        if noun == "up":
            try: 
                noun in player.location.exits
            except:
                story_functions.story_print(f"There is no path {noun}.")
            finally:
                story_functions.story_print("You climb the stairs.")
                player.location = player.location.floor_access[noun]
                story_functions.story_print(player.location.description)
        else:
            try:
                noun in player.location.exits
            except:
                story_functions.story_print(f"There is no path {noun}.")
            finally:
                story_functions.story_print("You descend the stairs.")
                player.location = player.location.floor_access[noun]
                story_functions.story_print(player.location.description)
    else:
        story_functions.story_print(f"{noun} is not a valid direction.")
        