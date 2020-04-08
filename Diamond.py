from Element import Element

class Diamond(Element):
    def __init__(self, diamondType=0):
        self.diamondType = diamondType
        if (self.diamondType not in range(2)):
            self.diamondType = 0 # Force to be a type 0 diamond
        if (self.diamondType == 0):
            super().__init__('RD', 'Red Diamond', None) # none for now
            self.addAmount = 3
            self.addType = 1  # ATK
        if (self.diamondType == 1):
            super().__init__('BD', 'Blue Diamond', None) # none for now
            self.addAmount = 3
            self.addType = 2  # DEF
