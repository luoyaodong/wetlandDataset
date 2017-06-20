#coding:utf8
import animalRelationDaoImpl

def findRelationToConention(animals,conventions):
    for con in conventions:
        if con[7] == None:
            continue
        for animal in animals:
            if animal[3] == None:
                continue
            if animal[3] in con[7]:
                animalRelationDaoImpl.addAnimalRelation(animal[0],animal[1],animal[3],con[7],con[0],con[1])
#给convention湿地公约寻找动物属性门纲目
def findRelationToAnimalAttribute(animals,conventions):
    for con in conventions:

        if con[7] == None:
            continue
        for animal in animals:
            if animal[3] == None:
                continue
            if animal[3] in con[7]:
                animalRelationDaoImpl.addAnimalAttributeRelation(animal[1],animal[2],animal[3],con[7],con[0])
