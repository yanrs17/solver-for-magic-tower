from Hero import Hero
from Monster import Monster
from Battle import Battle
from Tower import Tower
from Floor import Floor
from Wall import Wall
from Door import Door
from Key import Key
from Diamond import Diamond
from Potion import Potion
from Element import Element


def getSurroundedCells(tower, coord, coordsDiscovered):

    def getLists(newCoord):
        cell = getObjectFromCoord(tower, newCoord)
        nulls = []
        collectibles = []
        consumables = []
        if (newCoord not in coordsDiscovered):
            if (cell is None):
                nulls.append(newCoord)
            elif (type(cell) in [Key, Diamond, Potion]):
                collectibles.append(newCoord)
            elif (type(cell) in [Door] or issubclass(type(cell), Monster)):
                consumables.append(newCoord)
        return (nulls, collectibles, consumables)

    (x,y,z) = coord
    nulls = []
    collectibles = []
    consumables = []
    # print(issubclass(Potion, Diamond))

    if (x > 0): # Not at top boundary
        newCoord = (x-1,y,z)
        lists = getLists(newCoord)
        nulls.extend(lists[0])
        collectibles.extend(lists[1])
        consumables.extend(lists[2])

    if (x < 11 - 1): # Not at bottom boundary
        newCoord = (x+1,y,z)
        lists = getLists(newCoord)
        nulls.extend(lists[0])
        collectibles.extend(lists[1])
        consumables.extend(lists[2])

    if (y > 0): # Not at left boundary
        newCoord = (x,y-1,z)
        lists = getLists(newCoord)
        nulls.extend(lists[0])
        collectibles.extend(lists[1])
        consumables.extend(lists[2])

    if (y < 11 - 1): # Not at right boundary
        newCoord = (x,y+1,z)
        lists = getLists(newCoord)
        nulls.extend(lists[0])
        collectibles.extend(lists[1])
        consumables.extend(lists[2])

    return (nulls, collectibles, consumables)

    # print(type(up) in [Key, Diamond, Potion] or up is None)

def getObjectFromCoord(tower, coord):
    (x,y,z) = coord
    return tower.floors[str(z)].map[x][y+1]

if __name__ == '__main__':
    tower = Tower('tower24')
    tower.addFloor('1')
    tower.printFloor(tower.floors['1'])
    coordsDiscovered = [tower.currentCoord]
    queue = [tower.currentCoord]
    nulls = []
    # collectibles = []
    consumables = []

    while (len(queue)):
        
        # Discover surrounded cell by BFS
        surroundedCells = getSurroundedCells(tower, queue.pop(0), coordsDiscovered)
        nulls.extend(surroundedCells[0])
        # collectibles.extend(surroundedCells[1])
        consumables.extend(surroundedCells[2])
        queue.extend(surroundedCells[0])
        coordsDiscovered.extend(surroundedCells[0])
        coordsDiscovered.extend(surroundedCells[1])
        coordsDiscovered.extend(surroundedCells[2])

        for collectible in surroundedCells[1]:
            cell = getObjectFromCoord(tower, collectible)
            if type(cell) == Key:
                tower.hero.addKey(cell.keyType)
            # print(type(cell) == Key)
            # print(.keyType ==)


        # print('nulls')
        # print(nulls)
        # print('consumables')
        # print(consumables)
        # print('coordsDiscovered')
        # print(coordsDiscovered)
        # print('\n')
        # break

    
    # mon = Monster('MN', 'Just a normal monster', None, 51, 12, 8, 5, 5)
    # battle = Battle(hero, mon)
