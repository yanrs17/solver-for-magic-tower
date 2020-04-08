from Element import *

class Creature(Element):
    def __init__(self, REP, NME, ICN, HP, ATK, DEF, GLD, EXP):
        super().__init__('HR', 'Hero', ICN)
        self.REP = REP
        self.NME = NME
        self.ICN = ICN
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.GLD = GLD
        self.EXP = EXP

    def attack(self):
        # Set ATK as default attack
        return self.ATK

    def defense(self):
        # Set DEF as default defence
        return self.DEF
    
    def isDead(self):
        return self.HP <= 0