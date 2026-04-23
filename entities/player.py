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
    if noun not in player.location.exits:
        story_functions.story_print(f"There is no path {noun}.")
        return
    
    if player.location.locked_door.get(noun):
        print(f"The door to the {noun} is locked.")
        return
    
    story_functions.story_print(f"You move {noun}.")
    player.location = player.location.exits[noun]
    story_functions.story_print(player.location.description)

def use_stairs(noun):
    if noun not in player.location.floor_access:
        story_functions.story_print(f"There is no path {noun}.")
        return
    
    if noun == "up":
        story_functions.story_print(f"You climb the stairs")
        player.location = player.location.floor_access[noun]
        story_functions.story_print(player.location.description)
        return
    
    story_functions.story_print("You descend the stairs.")
    player.location = player.location.floor_access[noun]
    story_functions.story_print(player.location.description)

        