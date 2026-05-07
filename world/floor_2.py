from world.rooms import room

room_list2 = []

#Create rooms
stairwell_1_down = room("First Stairwell Bottom", None, None)
stairwell_1_down.description = ("This floor is notably cooler, the only thing of note is the door to the north")
stairwell_1_down.visited_description = ("You are at the bottom of the stairs from the first floor. There is a door to the north.")
room_list2.append(stairwell_1_down)

stone_mouth = room("Mouth Room", None, None)
stone_mouth.description = ("This room contains a door to the east. Dominating the north wall is a large relief of an open, fanged mouth. The sight of it fills you with dread.")
stone_mouth.visited_description = ("You are in the room with the stone mouth. There are doors to the south and east.")
room_list2.append(stone_mouth)

key_room = room("Key Room", None, None)
key_room.description = ("This is a nondescript room with a door on the south wall, the onlything that catches your eye is a dull glint on the floor by the east wall. Upon closer inspection you find a slightly rusted key.")
key_room.visited_description = ("This is the room where you found the rusted key. There are doors to the north and south.")
room_list2.append(key_room)

pack_room = room("Pack Room", None, None)
pack_room.description = ("This room is in rough shape, the flooring is loose and cracked. Parts of the walls have fallen away revealing the earth beyond. There is a simple leather pack on the floor in the south-west corner and a door on the south wall.")
pack_room.visited_description = ("This is the room where you found the discarded pack. There are doors to the north and south.")
room_list2.append(pack_room)

encounter_room_1 = room("Encounter Room", None, None)
encounter_room_1.description = ("The moment you enter this room the hairs on the back of your neck stand on end. You hear the light taps on the floor in front of you as a single human hand scurries out of the dark corner of the room, running on its fingers. A single strikingly blue eye peers at you from the back of the hand, the bones of the wrist and forearm have been twisted into a tail tipped with a blade that hangs above the hand like a scorpion.")
encounter_room_1.visited_description = ("This is the room where you first encountered the Skitter Hands. There are doors to the north and south.")
room_list2.append(encounter_room_1)

locked_door_room = room("Locked Room", None, None)
locked_door_room.description = ("This room is mecifully empty, save for a lantern placed on the floor to your left and a door on the west wall.")
locked_door_room.visited_description = ("This is the room where you found the lantern, the stairwell down is to the west and there is a door ont he north wall.")
locked_door_room.locked_door["west"] = True
room_list2.append(locked_door_room)

stairwell_2 = room("Second Stairwell", None, None)
stairwell_2.description = ("The stairwell before you is massive, it circles the edge of the room and decends down into the darkness. There are no torches here, it would not be safe to decend without a light.")
stairwell_2.visited_description = ("You are at the top of the stairs leading down to the third level, there is a door to the east.")
room_list2.append(stairwell_2)
