from world.rooms import room

room_list1 = []

# Create rooms
entrance = room("The Entrance", None, None)
entrance.description = ("The room is small, there is a door to the North of you, and to the South is the heavy iron gate, shut tight against the world")
entrance.visited_description = ("This is the room you woke up in, the gate to the outside remains locked with no way to open it.")
room_list1.append(entrance)

stairwell_1 = room("Stairwell", None, None)
stairwell_1.description = ("This room is the same size as The Entrance, it contains a few torches and a stairwell leading down into the darkness.")
stairwell_1.visited_description = ("You are at the top of the stairs on the first floor, the entrance is to the south.")
room_list1.append(stairwell_1)
