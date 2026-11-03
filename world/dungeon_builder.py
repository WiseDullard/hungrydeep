from world import floor_1, floor_2, floor_3, floor_4
from entities import monster
from entities import items

# floor 1 links
floor_1.entrance.exits["north"] = floor_1.stairwell_1

floor_1.stairwell_1.exits["south"] = floor_1.entrance
floor_1.stairwell_1.floor_access["down"] = floor_2.stairwell_1_down

# floor 2 links
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
floor_2.stairwell_2.floor_access["down"] = floor_3.stairwell_2_down

# floor 3 links
floor_3.stairwell_2_down.exits["east"] = floor_3.skeleton_room
floor_3.stairwell_2_down.floor_access["up"] = floor_2.stairwell_2

floor_3.skeleton_room.exits["west"] = floor_3.stairwell_2_down
floor_3.skeleton_room.exits["north"] = floor_3.feather_root_room

floor_3.feather_root_room.exits["south"] = floor_3.skeleton_room
floor_3.feather_root_room.exits["west"] = floor_3.encounter_room_2

floor_3.encounter_room_2.exits["east"] = floor_3.feather_root_room
floor_3.encounter_room_2.exits["north"] = floor_3.brazier_room

floor_3.brazier_room.exits["south"] = floor_3.encounter_room_2
floor_3.brazier_room.exits["north"] = floor_3.stairwell_3

floor_3.stairwell_3.exits["south"] = floor_3.brazier_room
floor_3.stairwell_3.floor_access["down"] = floor_4.stairwell_3_bottom

# floor 4 links
floor_4.stairwell_3_bottom.exits["south"] = floor_4.heart_chamber_section_1
floor_4.stairwell_3_bottom.floor_access["up"] = floor_3.stairwell_3

floor_4.heart_chamber_section_1.exits["south"] = floor_4.heart_chamber_section_2
floor_4.heart_chamber_section_1.exits["north"] = floor_4.stairwell_3_bottom

floor_4.heart_chamber_section_2.exits["south"] = floor_4.heart_chamber_section_3
floor_4.heart_chamber_section_2.exits["north"] = floor_4.heart_chamber_section_2

floor_4.heart_chamber_section_3.exits["north"] = floor_4.heart_chamber_section_2

# add items to rooms
# floor 2
floor_2.key_room.items.append(items.rusted_key)
floor_2.pack_room.items.append(items.leather_cloak)
floor_2.locked_door_room.items.append(items.lantern)

#floor 3
floor_3.skeleton_room.items.append(items.sword)
floor_3.feather_root_room.items.append(items.feather_root)
floor_3.brazier_room.items.append(items.writing_on_wall)
floor_3.brazier_room.items.append(items.brazier)

#floor 4
floor_4.heart_chamber_section_3.items.append(items.dungeon_heart)

# add entities to rooms
# floor 2
skitter_hand = monster.skitter_hand()
skitter_hand.name = ("Skitter Hand")
floor_2.encounter_room_1.entities += [skitter_hand]

# floor 3
skitter_hand_1 = monster.skitter_hand()
skitter_hand_1.name = ("Skitter Hand 1")

skitter_hand_2 = monster.skitter_hand()
skitter_hand_2.name = ("Skitter Hand 2")

skitter_hand_3 = monster.skitter_hand()
skitter_hand_3.name = ("Skitter Hand 3")

ghost_1 = monster.ghost()
ghost_1.name = ("Ghost 1")

ghost_2 = monster.ghost()
ghost_2.name = ("Ghost 2")

ghost_3  = monster.ghost()
ghost_3.name = ("Ghost 3")

floor_3.encounter_room_2.entities += [skitter_hand_1, skitter_hand_2, skitter_hand_3]

floor_3.brazier_room.entities += [ghost_1, ghost_2, ghost_3]

# floor 3
hollow_giant = monster.hollow_giant()
hollow_giant.name = ("Hollow Giant")

floor_4.heart_chamber_section_2.entities += [hollow_giant]