class item(object):
    def __init__(self, name, description, equipped, damage):
        self.name = name
        self.description = description
        self.equipped = equipped
        self.damage = damage


dagger = item("dagger", None, False, 10)
dagger.description = ("A small dagger, it used to belong to your father.")

food = item("food", None, False, None)
food.description = ("Two days worth of food, you're not sure why they gave you this, nobody comes back from the deep.")

rusted_key = item("key", None, False, None)
rusted_key.description = ("A small, slightly rusted iron key.")


