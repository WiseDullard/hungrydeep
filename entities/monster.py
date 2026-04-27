class monster(object):
    def __init__(self, name, health, defence, damage):
        self.name = name
        self.health = health
        self.defence = defence
        self.damage = damage

skitter_hand = monster("Skitter-hand", 20, 0, 10)

ghost = monster("Ghost", 100, 100, 30)

hollow_giant = monster("Hollow Giant", 100, 100, 50)