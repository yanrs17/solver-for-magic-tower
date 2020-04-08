from Hero import Hero

# Each Tower is a state of the game
class Tower:
    def __init__(self, towerName, floors={}, currentCoord=(10,5,1), hero=Hero(1000, 10, 10), coordsDiscovered=[], consumables=[]):
        self.towerName = towerName
        self.floors = floors
        self.currentCoord = currentCoord
        # self.initFloorName = str(self.currentCoord[2])
        self.hero = hero
        self.coordsDiscovered = coordsDiscovered
        if self.coordsDiscovered == []:
            self.coordsDiscovered = [self.currentCoord]
        self.consumables = consumables # Monsters, Doors etc
        # Add hero to floor?
        # self.addFloor(self.initFloorName)
        # self.printFloor(self.floors[self.initFloorName])

    def printFloor(self, floor):
        floor.printFloor()

    def addFloor(self, floorName):
        loaded = __import__('towers.{0}.{1}'.format(self.towerName, floorName))
        floor = getattr(getattr(loaded, self.towerName), floorName).loadFloor()
        self.floors[floorName] = floor
