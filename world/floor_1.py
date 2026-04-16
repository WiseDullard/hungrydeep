from rooms import room
from floor_2 import room_list2

# Create container for rooms
room_list1 = []

# Create rooms
entrance = room("The Entrance", None)
entrance.description = "The room is small, there is a door to the North of you, and to the South is the heavy iron gate, shut tight against the world"

stairwell_1 = room("Stairwell", None)
stairwell_1.description = ("This room is the same size as The Entrance, it contains a few torches and a stairwell leading down into the darkness.")

#Add rooms to Floor_1
room_list1.append[entrance, stairwell_1]

# Connect rooms
entrance.exits.append["north"] = stairwell_1

stairwell_1.exits.append["south"] = entrance
stairwell_1.exits.append["down"] = room_list2[0]
