from Creature import Creature

class Hero(Creature):
    def __init__(self, HP, ATK, DEF):
        super().__init__('HR', 'Hero', None, HP, ATK, DEF, 0, 0)
        self.keys = [0,1,1] # Default keys

    def addGold(self, gold):
        self.GLD += gold

    def addExp(self, exp):
        self.EXP += exp
    
    def addKey(self, keyType):
        self.keys[keyType] += 1