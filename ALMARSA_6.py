# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:47:26 2019

@author: Almarsa
"""

class Bird():
    def __init__(self):
        self.wings = True
        self.fur = True
        self.fly = True

    def isFly(self) :
        return self.fly
    
    def changeFly(self, command) :
        if command == 1 :
            self.fly = False
        else:
            self.fly = True
            

parrot = Bird()
parrot.changeFly(1)

if parrot.isFly() == True:
    print('parrot can fly')
elif parrot.isFly() == False:
    print('parrot is sick')
    
class penguin(Bird):
    def __init__(self):
        self.fly = False
        
    def isSwim(self):
        return True

igo = penguin()

if igo.isFly() == True:
    print('impossible')
elif igo.isFly() == False:
    print('igo cant fly')
    
if igo.isSwim() == True:
    print('igo is swim')
elif igo.isSwim() == False:
    print('igo is lazy')
    
    

