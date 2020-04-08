from Element import Element

class Door(Element):
    def __init__(self, doorType=0):
        # Type: 0, 1, 2
        # 0: Yellow, 1: Blue, 2: Red
        self.doorType = doorType
        if (self.doorType not in range(3)):
            self.doorType = 0 # Force to be a type 1 door
        typeDict = {0: 'YG', 1: 'BG', 2: 'RG'}
        # YG for yellow gate, BG for blue gate, RG for red gate
        super().__init__(typeDict[self.doorType], typeDict[self.doorType], None) # none for now
