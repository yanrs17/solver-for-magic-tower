from Element import Element

class Potion(Element):
    def __init__(self, potionType=0):
        self.potionType = potionType
        if (self.potionType not in range(2)):
            self.potionType = 0 # Force to be a type 0 potion
        if (self.potionType == 0):
            super().__init__('RP', 'Red Portion', None) # none for now
            self.addAmount = 200
            self.addType = 0  # HP
        if (self.potionType == 1):
            super().__init__('BP', 'Blue Portion', None) # none for now
            self.addAmount = 500
            self.addType = 0  # HP
