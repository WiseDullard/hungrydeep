import time

from entities import items
from world.floor_1 import room_list1
from world.floor_2 import room_list2
from world.floor_3 import room_list3
from world.floor_4 import room_list4
from world import dungeon_builder
from story import story_functions

sleep = time.sleep

class Player(object):
    def __init__(self, location, health, defence):
        self.location = location
        self.health = health
        self.defence = defence
        self.inventory = []
        self.weapon = None
        self.is_alive = True
        self.previous_room = None
        

player = Player(room_list1[0], 100, 0)
player.inventory += [items.dagger, items.food]

#Playtest code, comment out when not needed.
#player.inventory += [items.lantern, items.flint_and_steel, items.sword, items.leather_cloak, items.feather_root]

#equip
def equip(noun):
    for item in player.inventory:
        if noun == item.name:
            if item.equippable == True:
                if item.is_weapon == True:
                    item.equipped = True
                    player.weapon = None
                    player.weapon = item
                    print(f"You equip the {item.name}")
                    sleep(1)
                    return
                item.equipped = True
                if item.defence > player.defence:
                    player.defence = item.defence
                    print(f"You equip the {item.name}")
                    sleep(1)
                    return
            else:
                print("you cannot equip that.")
                sleep(1)
                return  

    
    #vowels = ["a", "e", "i", "o", "u"]
    if noun and noun[0].lower() in "aeiou":
        print(f"You do not have an {noun}.")
    else:
        print(f"You do not have a {noun}.")
    return
        

#inspecting
def inspect(noun):
    if noun == "inventory":
        print("You are carrying:")
        for item in player.inventory:
            print(item.name)
            sleep(1)
        return
    if noun in ["room", "area", "location"]:
        if player.location.visited == False:
            story_functions.story_print(player.location.description)
        else:
            story_functions.story_print(player.location.visited_description)
        return
    
    for item in player.inventory:
        if noun == item.name:
            story_functions.story_print(item.description)
            return
        
    for item in player.location.items:
        if noun == item.name:
            story_functions.story_print(item.description)
            return
        
    print(f"You do not have a {noun}.")
    sleep(1)
    return
    


#handle movement
def move(noun):
    if player.location.name.lower() in ("heart chamber-middle", "heart chamber-by the heart"):
        if noun == "north":
            print("You have come too far, there is no turning back now.")
            sleep(1)
            return
    
    if noun not in player.location.exits:
        story_functions.story_print(f"There is no path {noun}.")
        sleep(1)
        return
    
    if player.location.locked_door.get(noun):
        print(f"The door to the {noun} is locked.")
        sleep(1)
        return
    
    if player.location.crumbling_wall.get(noun):
        print(f"There is no path {noun}, only a wall in rough shape. You notice the smoke slowly drifting through cracks in the wall.")
        sleep(1)
        return

    story_functions.story_print(f"You move {noun}.")
    player.previous_room = player.location
    player.location = player.location.exits[noun]
    n = 0
    for item in player.inventory:
        if item.name == "lantern":
            lantern = player.inventory[n]
        else:
            n += 1

    if player.location.visited == False:
        if player.location.name.lower() == "heart chamber-by the stairwell":
            
            if lantern.is_lit == False:
                story_functions.story_print("You get the feeling the chamber you are in is massive, the only thing you can see is a faint red glow pulsing slowly at the far end of the chamber.")
                return
        if player.location.name.lower() == "heart chamber-middle":
            if lantern.is_lit == False:
                story_functions.story_print("The shuffling sound gets louder, something large looms in the darkness in front of you. You skirt around the source of the noise and continue through the chamber. You are left alone.")
                return
        story_functions.story_print(player.location.description)
        player.location.visited = True
    else:
        story_functions.story_print(player.location.visited_description)

#separate code for using stairs
def use_stairs(noun):
    if noun not in player.location.floor_access:
        print(f"There is no path {noun}.")
        sleep(1)
        return
    
    if player.location.name.lower() in ("second stairwell", "third stairwell"):
        n = 0
        for item in player.inventory:
            if item.name == "lantern":
                lantern = player.inventory[n]
            else:
                n += 1
        if lantern.is_lit == False:
            print("It would not be safe to use these stairs without a light.")
            sleep(1)
            return
        
    if noun == "up":
        print(f"You climb the stairs")
        sleep(1)
        player.location = player.location.floor_access[noun]
        story_functions.story_print(player.location.description)
        return
    else:
        print("You descend the stairs.")
        sleep(1)
        player.previous_room = player.location
        player.location = player.location.floor_access[noun]
        story_functions.story_print(player.location.description)
        return

#picking up and dropping items
def get(noun):
    for item in player.location.items:
        if noun == "cloak":
            if item.name == "cloak":
                player.inventory.append(item)
                player.location.items.remove(item)
                story_functions.story_print("As you pick up the cloak you hear some small items clatter to the floor, you look down to see a flint-and-steel laying at your feet. They must have been wrapped up in the cloak.")
                player.location.items.append(items.flint_and_steel)
                return
            else:
                print(f"There is no {noun} in the room.")
                sleep(1)
                return
        
        if noun == item.name:
            player.inventory.append(item)
            player.location.items.remove(item)
            print(f"You pick up the {item.name}.")
            sleep(1)
            return
    
        else:
            print(f"There is no {noun} in the room.")
            sleep(1)
            return
    
def drop(noun):
    if noun in player.inventory:
        player.location.items.append(noun)
        player.inventory.remove(noun)
        print(f"You drop the {noun} on the floor.")
        sleep(1)
        
    else:
        print(f"You do not have a {noun}.")
        sleep(1)

#using items
def use_item(noun):
    for item in player.inventory:
        if noun == item.name:
            if item.name == "key":
                if player.location.locked_door["west"] == True:
                    print("You unlock the door.")
                    sleep(1)
                    player.location.locked_door["west"] = False
                    return
                else:
                    print("You have already unlocked the door.")
                    sleep(1)
                    return
            
            if item.name == "sword":
                if player.location.name == "brazier room":
                    if player.location.crumbling_wall["north"] == True:
                        story_functions.story_print("You use the point of your sword to pry at the space between bricks. After a few minutes of work, the bricks begin to fall away revealing a space behind the wall.")
                        player.location.crumbling_wall["north"] = False
                        return
                    else:
                        story_functions.story_print("You see nothing to use the sword on, you have already opened the wall.")
                        return
                
                if player.location.name.lower == "heart chamber-by the heart":
                    story_functions.story_print("You plunge your sword deep into the heart. A low rumble rips through the chamber, as much vibration as sound, as if stone could scream. The heart writhes as blood pours from the wound and from between the surrounding bricks.")
                else:
                    print("You do not see any reason to use your sword.")
                    sleep(1)
                    return
                
            elif item.name == "flint-and-steel":
                if items.lantern in player.inventory:
                    if items.lantern.is_lit == False:
                        items.lantern.is_lit = True
                        print("You light the lantern.")
                        sleep(1)
                        return
                    else:
                        print("The lantern is already lit.")
                        sleep(1)
                        return
                else:
                    print("You have nothing to light with the flint-and-steel.")
                    sleep(1)
                    return

            else:
                print(f"You see no reason to use the {item.name}.")
                sleep(1)

#game over
def game_over():
    story_functions.story_print("As you fall to the floor and your conciousness fades, red vines emerge from between the flagstones and wrap themselves around you. The depths have claimed you.")
    print("--- Game Over ---")
    sleep(1)
    print("Thanks for playing!")
    exit()
    

