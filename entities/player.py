from items import dagger, rations
from world.floor_1 import entrance


class player(object):
    def __init__(self, location):
        self.inventory = []
        self.location = location

player.inventory.append(dagger, rations)
player.location = entrance

#handle movement
def move(verb, noun):
    direction = ["north", "east", "south", "west", "up", "down"]
    if verb in ["move", "go", "travel", "walk"]:
        if noun in direction:
            player.location = player.location.exits[noun]