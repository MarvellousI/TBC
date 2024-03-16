# -*- coding: utf-8 -*-
"""
tbcstart.py
Created on Wed Mar 13 10:29:33 2024

@author: marve
""" 
import random

class Character (object):
    
    def __init__(self, name = "default name", hitPoints = 6, hitChance = 8, maxDamage = 8, armor = 1):
        
        
        super().__init__() 
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor 
        
        @property 
        def name(self):
            return self.name 
        
        @name.setter
        def name(self, value):
            self.__name = value
            
        @property 
        def hitPoints(self):
            return self.__hitPoints 
        
        @hitPoints.setter 
        def hitPoints(self, value):
            self.__hitPoints = value
            
        @property 
        def hitChance(self):
            return self.__hitChance
        
        @hitChance.setter 
        def hitChance(self, value):
            self.__hitChance =value 
            
        @property 
        def maxDamage(self):
            return self.__maxDamage
        
        @maxDamage.setter 
        def maxDamage(self, value): 
            self.__maxDamage = value
            
        @property
        def armor(self):
            return self._armor
        
        @armor.setter 
        def armor(self, value):
            self.__maxDamage = value
            
                 
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """

        out = default
    
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
    
        return out
                            
                            
def printStats(self): 
            print(f"""
{self.name}                  
hit Points: {self.hitPoints}
hit Chance: {self.hitChance}
max damage: {self.maxDamage}
armor: {self.armor}""")

def hit(self, Runner):
        hitRand = random.randint(0, 100)
        dmgNum = random.randint(1, self.maxDamage)
        if hitRand <= self.hitChance:
            print(f"""{self.name} hits {Runner.name}
                        for {dmgNum} points of damage
                        {Runner.name}'s armor absorbs {Runner.armor} points of damage
              """)
            if dmgNum > Runner.armor:
                dealtDmg = dmgNum - Runner.armor
                Runner.hitPoints -= dealtDmg
        else:
            print(f"{self.name} missed")
    
 

def fight(Chaser, Runner):
    keepGoing = True
    while keepGoing:

       hit(Chaser, Runner)
       hit(Runner, Chaser)
       

       print(f"{Chaser.name}: {Runner.hitPoints} HP")
       print(f"{Runner.name}: {Chaser.hitPoints} HP")

       if Chaser.hitPoints > 0:
            if Runner.hitPoints > 0:
                userChoice = input("Press ENTER for another round or Q to quit: ")
                if userChoice == "Q":
                    keepGoing = False
            else:
                print(f"{Chaser.name} wins")
                keepGoing = False
       else:
            print(f"{Runner.name} wins")
            keepGoing = False

def main():
      c = Character()
      printStats(c)

if __name__ == "__main__":
    main()
    
    

    
                
            
            
    
