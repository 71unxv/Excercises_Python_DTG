# -*- coding: utf-8 -*-
# =============================================================================
# Object Oriented Programming
# =============================================================================

class Bird():
    def __init__(self):
        self.wings = True
        self.fur = True
        self.__fly = True
    def isFly(self):
        return self.__fly
    def changeFly(self,command):
        if command == 1:
            self.__fly = False
        else:
            self.__fly = True
class Penguin(Bird):
    def __init__(self):
        self.isFly == False
    def isSwim(self):
        return True

Elang = Bird()

Elang.changeFly(1)

if Elang.isFly() == True:
    print('Elang bisa terbang')
elif Elang.isFly() == False:
    print('Elang sakit')
#    
#Igo = Penguin()
#if Igo.isSwim() == True:
#    print('Igo Bisa Berenang')
#else:
#    print('Igo tidak bisa berenang')