class item(object):
    def __init__(self, name, description, equippable, equipped, damage, defence):
        self.name = name
        self.description = description
        self.equippable = equippable
        self.equipped = equipped
        self.damage = damage
        self.defence = defence
        self.can_be_carried = True
        self.is_weapon = False
        self.lightable = False
        self.is_lit = False


dagger = item("dagger", None, True, False, 10, None)
dagger.description = ("A small dagger, it used to belong to your father.")
dagger.is_weapon = True

food = item("food", None, False, False, None, None)
food.description = ("Two days worth of food, you're not sure why they gave you this, nobody comes back from the deep.")

rusted_key = item("key", None, False, False, None, None)
rusted_key.description = ("A small, slightly rusted iron key.")

leather_cloak = item("cloak", None, True, False, None, 5)
leather_cloak.description = ('A tanned leather cloak, in surprisingly good condition. The initials "A.B." are embroidered near the clasp.')

flint_and_steel = item("flint-and-steel", None, False, False, None, None)
flint_and_steel.description = ("A piece of flint the size of your palm and a steel strike. Useful for starting fires, similar to the one you used back home.")

lantern = item("lantern", None, False, False, None, None)
lantern.description = ("A standard lantern, made of iron and, luckily, still mostly filled with oil.")
lantern.lightable = True

sword = item("sword", None, True, False, 20, None)
sword.description = ("A short sword, a little dull but still usable.")
sword.is_weapon = True

brazier = item("brazier", None, False, False, None, None)
brazier.description = ("A bronze brazier with three feet and ornate detailing, it appears to have been used for some form of ceremony.")
brazier.can_be_carried = True
brazier.lightable = True

feather_root = item("feather-root", None, False, False, None, None)
feather_root.description = ("You have seen your grandmother use feather-root for smudging. Highly flamable, it produces a lot of smoke that is said to banish spirits and protect the home.")

writing_on_wall = item("writing", None, False, False, None, None)
writing_on_wall.description = ('The words are srached into the stone itself, you are unsure how they were made, they read "IS IT A HOLE OR AN EYE".')
writing_on_wall.can_be_carried = False

dungeon_heart = item("heart", None, False, False, None, None)
dungeon_heart.description = ('As you approach the heart you hear a voice in your head, it seems to ooze from the stone around you and says "You are surprisingly resiliant, more than those who abandoned you here would think. Feast upon me and take eternal vengance on them."')
dungeon_heart.can_be_carried = False