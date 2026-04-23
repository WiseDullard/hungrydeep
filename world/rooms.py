class room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.floor_access = {}
        self.locked_door = {}
        self.items = []

