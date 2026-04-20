from entities.items import dagger, rations
from world.floor_1 import entrance


class player(object):
    def __init__(self, location):
        self.inventory = []
        self.location = location

player.inventory.append(dagger, rations)
player.location = entrance

#handle movement
def move(noun):
    direction = ["north", "east", "south", "west"]
    if noun in direction:
        print(f"You move {player.location.exits[noun]}")
        player.location = player.location.exits[noun]
    else:
        print(f"there is no path {noun}.")

def use_stairs(noun):
    if noun in ["up", "down"]:
        if noun == "up":
            print("You climb up the stairs.")
            player.location = player.location.floor_access[noun]
        else:
            print("You climb down the stairs.")
            player.location = player.location.floor_access[noun]
    else:
        print(f"There is no path {noun}.")