from entities import items
from world.floor_1 import room_list1
from world.floor_2 import room_list2
from world import dungeon_builder
from story import story_functions


class Player(object):
    def __init__(self, location, health, defence):
        self.location = location
        self.health = health
        self.defence = defence
        self.inventory = []
        

player = Player(room_list1[0], 100, 0)
player.inventory += [items.dagger, items.food]

#inspecting
def inspect(noun):
    if noun == "inventory":
        print("You are carrying:")
        for item in player.inventory:
            print(item.name)
        return
    if noun in ["room", "area", "location"]:
        story_functions.story_print(player.location.description)
        return
    
    for item in player.inventory:
        if noun == item.name:
            story_functions.story_print(item.description)
            return
        
    print(f"You do not have a {noun}.")
    return
    


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

#separate code for using stairs
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

#picking up and dropping items
def get(noun):
    if noun in player.location.items:
        player.items.append(noun)
        player.location.items.remove(noun)
        print(f"You pick up {noun}.")
    
    else:
        print(f"There is no {noun} in the room.")
    
def drop(noun):
    if noun in player.inventory:
        player.location.items.append(noun)
        player.inventory.remove(noun)
        print(f"You drop the {noun} on the floor.")
        
    else:
        print(f"You do not have a {noun}.")

