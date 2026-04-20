from world import floor_1, floor_2

#floor 1 links
floor_1.entrance.exits["north"] = floor_1.stairwell_1
floor_1.stairwell_1.exits["south"] = floor_1.entrance
floor_1.stairwell_1.floor_access["down"] = floor_2.stairwell_1_down
