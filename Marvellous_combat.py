# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:48:29 2024

@author: marve
"""

import Marvellous_TBC

def main():
    runner = Marvellous_TBC.Character()
    runner.name = "Runner"
    runner.hitPoints = 6
    runner.hitChance = 8
    runner.maxDamage = 8
    runner.armor = 1
    
    chaser = Marvellous_TBC.Character("Chaser", 7, 8, 7, 1)

    Marvellous_TBC.printStats(chaser)
    Marvellous_TBC.printStats(runner)

    Marvellous_TBC.fight(runner, chaser)

if __name__ == "__main__":
    main()
    