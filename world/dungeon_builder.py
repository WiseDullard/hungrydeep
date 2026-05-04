from world import floor_1, floor_2
from entities import monster

#floor 1 links
floor_1.entrance.exits["north"] = floor_1.stairwell_1

floor_1.stairwell_1.exits["south"] = floor_1.entrance
floor_1.stairwell_1.floor_access["down"] = floor_2.stairwell_1_down

#floor 2 links
floor_2.stairwell_1_down.floor_access["up"] = floor_1.stairwell_1
floor_2.stairwell_1_down.exits["north"] = floor_2.stone_mouth

floor_2.stone_mouth.exits["south"] = floor_2.stairwell_1_down
floor_2.stone_mouth.exits["east"] = floor_2.key_room

floor_2.key_room.exits["west"] = floor_2.stone_mouth
floor_2.key_room.exits["south"] = floor_2.pack_room

floor_2.pack_room.exits["north"] = floor_2.key_room
floor_2.pack_room.exits["south"] = floor_2.encounter_room_1

floor_2.encounter_room_1.exits["north"] = floor_2.pack_room
floor_2.encounter_room_1.exits["south"] = floor_2.locked_door_room

floor_2.locked_door_room.exits["north"] = floor_2.encounter_room_1
floor_2.locked_door_room.exits["west"] = floor_2.stairwell_2

floor_2.stairwell_2.exits["east"] = floor_2.locked_door_room


# add entities to rooms
skitter_hand1 = monster.skitter_hand
skitter_hand2 = monster.skitter_hand
floor_2.encounter_room_1.entities += [skitter_hand1, skitter_hand2]
