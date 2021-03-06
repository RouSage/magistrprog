from CharacterModule import Character

#Класс описывающий главного персонажа
class MainCharacter(Character):
    def __init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount,Motion, name, hp, exp, lvl, damage, isEffect, LeftANIM, RightANIM):
        Character.__init__(self, ID, TYPE, MainList, x, y, MainPick, AnimCount, Motion, name, hp, LeftANIM, RightANIM)
        self.__LVL = lvl
        self.__damage = damage
        self.__isEffect = isEffect
        
        
#Инкапсуляция
    def getLVL(self):
        return self.__LVL

    def setLVL(self, lvl):
        self.__LVL = lvl

    def getDamage(self):
        return self.__damage

    def setDamage(self, dam):
        self.__damage = dam

    def getIsEffect(self):
        return self.__isEffect

    def setIsEffect(self, isef):
        self.__isEffect = isef
