class item(object):
    def __init__(self, name, description, equippable, equipped, damage):
        self.name = name
        self.description = description
        self.equippable = equippable
        self.equipped = equipped
        self.damage = damage
        self.is_weapon = False


dagger = item("dagger", None, True, False, 10)
dagger.description = ("A small dagger, it used to belong to your father.")
dagger.is_weapon = True

food = item("food", None, False, False, None)
food.description = ("Two days worth of food, you're not sure why they gave you this, nobody comes back from the deep.")

rusted_key = item("key", None, False, False, None)
rusted_key.description = ("A small, slightly rusted iron key.")

leather_cloak = item("leather cloak", None, True, False, None)
leather_cloak.description = ('A tanned leather cloak, in surprisingly good condition. The initials "A.B." are embroidered near the clasp.')


