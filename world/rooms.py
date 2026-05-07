class room(object):
    def __init__(self, name, description, visited_description):
        self.name = name
        self.description = description
        self.visited_description = visited_description
        self.visited = False
        self.exits = {}
        self.floor_access = {}
        self.locked_door = {}
        self.items = []
        self.entities = []

