from Floor import Floor
from Hero import Hero
from Wall import Wall
from Door import Door
from Key import Key
from Monster import *
from Potion import Potion
from Diamond import Diamond

def loadFloor():
    floor = Floor(1, '1')

    # Walls
    floor.batchAddElements(Wall(),1,0,1,9)
    floor.batchAddElements(Wall(),2,9,6,9)
    floor.batchAddElements(Wall(),6,5,6,8)
    floor.batchAddElements(Wall(),3,3,10,3)
    floor.batchAddElements(Wall(),8,4,8,10)
    floor.batchAddElements(Wall(),9,7,10,7)
    floor.batchAddElements(Wall(),2,5,4,5)
    floor.batchAddElements(Wall(),4,6,4,7)
    floor.addElement(Wall(),4,0)
    floor.addElement(Wall(),4,2)
    floor.addElement(Wall(),7,0)
    floor.addElement(Wall(),7,2)

    # Doors
    floor.addElement(Door(2),8,5)
    floor.addElement(Door(),2,3)
    floor.addElement(Door(),4,1)
    floor.addElement(Door(),7,1)
    floor.addElement(Door(),5,5)
    floor.addElement(Door(),8,9)

    # Keys
    floor.addElement(Key(),0,2)
    floor.addElement(Key(),3,0)
    floor.addElement(Key(),5,0)
    floor.addElement(Key(),9,2)
    floor.addElement(Key(),10,2)
    floor.addElement(Key(2),9,4)
    floor.addElement(Key(),2,7)
    floor.addElement(Key(),3,7)
    floor.addElement(Key(),9,8)
    floor.addElement(Key(1),6,2)
    floor.addElement(Key(1),9,10)
    floor.batchAddElements(Key(),10,8,10,10)

    # Monsters
    floor.addElement(HeadSlime(),0,3)
    floor.addElement(HeadSlime(),0,5)
    floor.addElement(HeadSlime(),5,7)
    floor.addElement(HeadSlime(1),0,4)
    floor.addElement(HeadSlime(2),4,8)
    floor.addElement(Skeleton(),2,2)
    floor.addElement(Skeleton(),3,1)
    floor.addElement(Skeleton(1),5,1)
    floor.addElement(Skeleton(1),8,1)
    floor.addElement(Bat(),5,6)
    floor.addElement(Witch(),5,8)
    floor.addElement(Orc(),9,9)

    # Potions
    floor.addElement(Potion(),2,0)
    floor.addElement(Potion(),2,6)
    floor.addElement(Potion(),3,6)
    floor.addElement(Potion(),2,8)
    floor.addElement(Potion(),3,8)
    floor.addElement(Potion(),9,0)
    floor.addElement(Potion(),10,0)
    floor.addElement(Potion(1),9,1)

    # Diamonds
    floor.addElement(Diamond(),3,2)
    floor.addElement(Diamond(1),6,0)

    return floor