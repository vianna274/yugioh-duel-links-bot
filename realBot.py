import pyscreenshot as ImageGrab
import os
import time
import win32api
import win32con
from numpy import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

x1 = 170
y1 = 442

x2 = 430
y1 = 442

x_start = 140
x_end = 480

y_start = 400
y_end = 760

""" IMAGES """
d1 = "d01.png"
d2 = "d02.png"
d3 = "d03.png"
d4 = "d04.png"
d5 = "d05.png"
d6 = "d06.png"
d7 = "d07.png"
d8 = "d08.png"
d9 = "d09.png"
d10 = "d10.png"
d11 = "d11.png"
d12 = "d12.png"
d13 = "d13.png"
d14 = "d14.png"
d15 = "d15.png"
d16 = "d16.png"
d17 = "d17.png"
d18 = "d18.png"
d19 = "d19.png"
d20 = "d20.png"
d21 = "d21.png"
d22 = "d22.png"
d23 = "d23.png"
d24 = "d24.png"
d25 = "d25.png"
d26 = "d26.png"
d27 = "d27.png"
d28 = "d28.png"
d29 = "d29.png"
d30 = "d30.png"
d31 = "d31.png"

bonusImage = "bonus.png"
screen = "screen.png"
duelImage = "duel.png"
nextImage = "next.png"
okImage = "ok.png"
autoDuelImage = "autoduel.png"
skipImage = "skip.png"
backImage = "back.png"

duelists = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31]

def screenShot():
    # fullscreen
    im = ImageGrab.grab_to_file(screen)

def slideLeft():
    xChanging = x1
    yChanging = y1
    while (xChanging <= x2):
        mousePos(xChanging,yChanging)
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN,
            xChanging,
            yChanging
        )
        xChanging+=1;
    mousePos(xChanging,yChanging)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP,
        xChanging,
        yChanging
    )

def mousePos(x,y):
    win32api.SetCursorPos((x,y))

def leftClick(x,y):
    mousePos(x,y)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN,
        0,
        0
        )
    time.sleep(1)
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP,
        0,
        0
    )

def searchOk():
    x,y = locateImage(screen,okImage)
    if x != 1:
        leftClick(x,y)
        print ("OK")
        return True
    return False

def searchNext():
    x,y = locateImage(screen,nextImage)
    if x != 1:
        leftClick(x,y)
        print ("NEXT")
        return True
    return False

def searchDuel():
    x,y = locateImage(screen,duelImage)
    if x != 1:
        leftClick(x,y)
        print ("DUEL")
        return True
    return False

def searchBack():
    x,y = locateImage(screen,backImage)
    if x != 1:
        leftClick(x,y)
        print ("BACK")
        return True
    return False

def searchAutoDuel():
    x,y = locateImage(screen,autoDuelImage)
    if x != 1:
        leftClick(x,y)
        print ("AUTODUEL")
        return True
    return False

def searchBonus():
    x,y = locateImage(screen,bonusImage)
    if x != 1:
        leftClick(x,y)
        print ("BONUS")
        return True
    return False

def searchSkip():
    x,y = locateImage(screen,skipImage)
    if x != 1:
        leftClick(x,y)
        print ("SKIP")
        return True
    return False

def searchDuelist():
    for duelist in duelists:
        x,y = locateImage(screen,duelist)
        if x != 1:
            leftClick(x,y)
            print ("DUELIST")
            return True
    return False

def locateImage(fullImage, partImage):
    img_rgb = cv2.imread(fullImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(partImage,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    try:
        return loc[1][0]+15, loc[0][0]+15
    except:
        return 1,1
    #for pt in zip(*loc[::-1]):
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #cv2.imwrite('res.png',img_rgb)

def main():
    while(True):
        #print ("COMECOU")
        start = True
        time.sleep(3)
        screenShot()
        searchBonus()
        if searchDuelist():
            while start:
                screenShot()
                if searchSkip():
                    start = False
            start = True
            while start:
                screenShot()
                if searchDuel():
                    start = False
            start = True
            while start:
                screenShot()
                if searchAutoDuel():
                    start = False
            start = True
            while start:
                screenShot()
                if searchOk():
                    start = False
            start = True
            while start:
                screenShot()
                if searchNext():
                    start = False
            start = True
            while start:
                screenShot()
                if searchOk():
                    start = False
            start = True
            while start:
                screenShot()
                if searchSkip():
                    start = False
        else:
            searchBack()
            slideLeft()






if __name__ == '__main__':
    main()
