import random, time
import numpy as np
import controler

lpDis = controler.Display()
lpDis.Clear()

clicked = True
game_over = False

patternX = []
patternY = []

while game_over == False:
    patNum = 0
    if clicked == True:
        x = random.randrange(0, 7)
        y = random.randrange(1, 8)
        patternX.append(x)
        patternY.append(y)
        while patNum <= len(patternX)-1:
            ix = patternX[patNum]
            iy = patternY[patNum]
            lpDis.setLED(ix, iy, 0, 0, 255)
            time.sleep(0.5)
            lpDis.setLED(ix, iy, 0, 0, 0)
            patNum+=1
        clicked = False
    
    patNum = 0
    while clicked != True:
        buts = lpDis.ButtonGet()
        ix = patternX[patNum]
        iy = patternY[patNum]
        print(ix, iy)
        if buts != []:
            if buts[0:2] == [8, 8] and buts[2]:
                game_over = True
                break

            if buts[0:2] == [ix, iy] and buts[2]:
                print("Correct, "+str(buts[0:2]))
                print("patNum: " + str(patNum))
                if patNum >= len(patternX)-1:
                    clicked = True
                else:
                    patNum+=1
                
            elif buts[0:2] != [ix, iy] and buts[2]:
                x, y = buts[0:2]
                print("Worng, "+str(buts[0:2])+" Should be ["+str(ix)+" , "+str(iy)+"]")
                lpDis.setLED(x, y, 255, 0, 0)
                lpDis.setLED(ix, iy, 0, 255, 0)
                time.sleep(1)
                game_over = True
                clicked = True
                break
    
lpDis.Clear()
lpDis.LiveMode()
lpDis.Close()