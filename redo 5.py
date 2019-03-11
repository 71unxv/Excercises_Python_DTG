class Bird():
    def __init__ (self) :
        self.wings = True
        self.fur = True
        self.fly = True
    
    def isFly(self) :
        return self.fly
    
    def changeFly(self, command):
        if command == 1:
            self.fly == False
        else :
        self.fly == True
            
class Penguin(Bird):
    def __init__ (self):
        self.fly = False
        
    def isSwim(self):
        return True
            
Parrot = Bird()
Igo = Penguin()


if Igo.isFly() == True:
    print('impossible')
elif Igo.isFly() == False:
    print('Igo Cant Fly')
    
if Igo.isSwim() == True:
    print('Igo can swim')
else:
    print('Igo is lazy')
    
if Parrot.isFly() == True:
    print('Parrot can fly')
elif Parrot.isFly() == False:
    print('Igo Cant Fly')
    

    