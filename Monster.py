from Creature import Creature

class Monster(Creature):
    def __init__(self, REP, NME, ICN, HP, ATK, DEF, GLD, EXP):
        super().__init__(REP, NME, ICN, HP, ATK, DEF, GLD, EXP)

class HeadSlime(Monster):
    # Slimes
    def __init__(self, kind=0):
        if (kind not in range(3)):
            kind = 0
        if (kind == 0):
            super().__init__('GS', 'Green Slime', None, 50, 20, 1, 1, 1)
        if (kind == 1):
            super().__init__('RS', 'Red Slime', None, 70, 15, 2, 2, 2)
        if (kind == 2):
            super().__init__('BS', 'Blue Slime', None, 200, 35, 10, 5, 5)

class Bat(Monster):
    # Bats
    def __init__(self, kind=0):
        if (kind not in range(3)):
            kind = 0
        if (kind == 0):
            super().__init__('SB', 'Small Bat', None, 100, 20, 5, 3, 3)
        if (kind == 1):
            super().__init__('LB', 'Large Bats', None, 150, 65, 30, 10, 8)
        if (kind == 2):
            super().__init__('RB', 'Red Bats', None, 550, 160, 90, 25, 20)

class Skeleton(Monster):
    # Skeletons
    def __init__(self, kind=0):
        if (kind not in range(3)):
            kind = 0
        if (kind == 0):
            super().__init__('SK', 'Skeleton', None, 110, 25, 5, 5, 4)
        if (kind == 1):
            super().__init__('SS', 'Skeleton Soldier', None, 150, 40, 20, 8, 6)
        if (kind == 2):
            super().__init__('SL', 'Skeleton Leader', None, 400, 90, 50, 15, 12)

class Witch(Monster):
    # Mages
    def __init__(self, kind=0):
        if (kind not in range(5)):
            kind = 0
        if (kind == 0):
            super().__init__('M1', 'Mage 1', None, 125, 50, 25, 10, 7)
        if (kind == 1):
            super().__init__('M2', 'Mage 2', None, 250, 120, 70, 20, 17)
        if (kind == 2):
            super().__init__('M3', 'Mage 3', None, 100, 200, 110, 30, 25)
        if (kind == 3):
            super().__init__('M4', 'Mage 4', None, 500, 400, 260, 47, 45)
        if (kind == 4):
            super().__init__('M5', 'Mage 5', None, 1500, 830, 730, 80, 70)

class Orc(Monster):
    # Orcs
    def __init__(self, kind=0):
        if (kind not in range(2)):
            kind = 0
        if (kind == 0):
            super().__init__('OC', 'Orc', None, 300, 75, 45, 13, 10)
        if (kind == 1):
            super().__init__('OW', 'Orc Warrior', None, 900, 450, 330, 50, 50)
