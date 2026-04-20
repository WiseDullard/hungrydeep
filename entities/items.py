class item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class weapon(item):
    def __init__(self, name, description, equipped, damage):
        self.name = name
        self.description = description
        self.equipped = equipped
        self.damage = damage

dagger = weapon("Dagger", None, False, 10)
dagger.description = ("A small dagger, it used to belong to your father.")

rations = item("Rations", None)
rations.description = ("Two days worth of food, you aren't sure why you have this, nobody comes back from the deep.")