X_RANGE = 11
Y_RANGE = 11

class Floor:
    def __init__(self, floorLevel, floorName):
        self.floorLevel = floorLevel
        self.floorName = floorName
        self.map = [[None for _ in range(X_RANGE)] for _ in range(Y_RANGE)]  # 2D list of 11 * 11
    
    def addElement(self, element, x, y):
        self.map[x][y] = element
    
    def removeElement(self, x, y):
        del self.map[x][y] # TODO SET TO None?

    def batchAddElements(self, element, x1, y1, x2, y2):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                self.map[x][y] = element # Pass by ref?

    def printFloor(self): 
        result = '_' * (X_RANGE * 5 + 1) + '\n'
        for row in self.map:
            result += '|'
            for item in row:
                if (item is None):
                    result += '    ' #████
                else:
                    result += item.REP
                result += ' '
            result = result[:-1]
            result += '|\n'

        result += '‾' * (X_RANGE * 5 + 1) 
        print(result)