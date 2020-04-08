from Element import Element

class Key(Element):
    def __init__(self, keyType=0):
        # Type: 0,1,2
        # 0: Yellow, 1: Blue, 2: Red
        self.keyType = keyType
        if (self.keyType not in range(3)):
            self.keyType = 0 # Force to be a type 0 key
        typeDict = {0: 'YK', 1: 'BK', 2: 'RK'}
        # YK is yellow key
        # BK is blue key
        # RK is red key
        super().__init__(typeDict[self.keyType], typeDict[self.keyType] + '匙', None) # none for now
