class monster(object):
    def __init__(self, name, health, defence, damage):
        self.name = name
        self.health = health
        self.defence = defence
        self.damage = damage
        self.is_alive = True

class skitter_hand(monster):
    def __init__(self):
        super().__init__("Skitter-hand", 20, 0, 10)
    

class ghost(monster):
    def __init__(self):
        super().__init__("Ghost", 100, 100, 30)
        self.distance = 3
    

class hollow_giant(monster):
    def __init__(self):
        super().__init__("Hollow-Giant", 100, 100, 40)
    
