# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:48:31 2019

@author: gayuh
"""

class Bird():
    def __init__(self):
        self.wings= True
        self.fur= True
        self.fly= True
    def isFly(self):
        return self.fly
    def changeFly(self, command):
        if command == 1:
            self.fly = False
        else:
            self.fly = True
    
if Parrot.isFly()==True:
    print('Parrot can fly')
elif Parrot.isFly() == False:
    print('Parrot is sick')
    
class Penguin(Bird):
    def __init__(self):
        self.fly = False
    def isSwim():
        return True

if Igo.isFLy() == True:
    print('impossible')
elif Igo.
    
Parrot = Bird()
Igo = Penguin()
