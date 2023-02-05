import random
import numpy as np
import controler

lpDis = controler.Display()
lpDis.Clear()

while True:
    for x in range(0, 9):
        for y in range(0, 9):
            lpDis.setLED(x, y, random.randrange(0, 50), random.randrange(0, 50), random.randrange(0, 50))
    
    buts = lpDis.ButtonGet()
    if buts != []:
        if buts[0:2] == [8, 8] and buts[2]:
            break
    
lpDis.Clear()
lpDis.LiveMode()
lpDis.Close()