import pyscreenshot as ImageGrab
import os
import time
import win32api
import win32con
from numpy import *

x1 = 170
y1 = 442

x2 = 430
y1 = 442

x_start = 140
x_end = 480

y_start = 400
y_end = 760

def screenShot():
    # fullscreen
    im = ImageGrab.grab()
    return im
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

def clickOk(im):
    if (im.getpixel((308,946)) == (255,255,255)):
        leftClick(308,946)
        print ("PRESSED OK")
        return 1
    return 0

def clickNext(im):
    if (im.getpixel((289,946)) == (255,255,255)):
        leftClick(289,946)
        print ("PRESSED NEXT")
        return 1
    return 0

def clickDuel(im):
    if (im.getpixel((273,872)) == (249,208,36)):
        leftClick(272,872)
        print ("PRESSED DUEL")
        return 1
    return 0

def clickBack(im):
    if (im.getpixel((32,962)) == (255,255,255)):
        leftClick(32,962)
        print ("PRESSED BACK")
        return 1
    return 0

def clickAutoDuel(im):
    if (im.getpixel((458,152)) == (253,253,253)):
        leftClick(458,152)
        print ("PRESSED AUTO-DUEL")
        return 1
    return 0

def clickDuelist(im,x,y):
    if (im.getpixel((x,y)) == (252,255,255)):
        leftClick(x,y)
        print ("PRESSED DUELIST")
    if (im.getpixel((x,y)) == (245,255,255)):
        leftClick(x,y)
        print ("PRESSED DUELIST")
    if (im.getpixel((x,y)) == (241,255,255)):
        leftClick(x,y)
        print ("PRESSED DUELIST")
    if (im.getpixel((x,y)) == (235,255,255)):
        leftClick(x,y)
        print ("PRESSED DUELIST")
    if (im.getpixel((x,y)) == (227,253,254)):
        leftClick(x,y)
        print ("PRESSED DUELIST")

def loopPlaying():
    stopDueling = 0
    while not stopDueling:
        im = screenShot()
        stopDueling = clickOk(im)

def main():
    dueling = 0
    stopDueling = 0
    xChanging = x_start
    yChanging = y_start
    while(True):
        print ("COMECOU")
        time.sleep(3)
        slideLeft()
        yChanging = y_start
        while (yChanging <= y_end):
            im = screenShot()
            xChanging = x_start
            duelClick = clickDuel(im)

            if duelClick:
                time.sleep(1)
                duelClick = 0

            #clickBack(im)
            nextClick = clickNext(im)
            okClick = clickOk(im)
            yChanging+=4

            if nextClick and okClick:
                dueling = 0
            print (xChanging, yChanging)

            while(xChanging <= x_end):
                #im = screenShot()
                #print (win32api.GetCursorPos())
                #print (im.getpixel(win32api.GetCursorPos()))
                #time.sleep(2)
                clickDuelist(im,xChanging,yChanging)
                if not dueling:
                    nextClick = 0
                    okClick = 0
                    dueling = clickAutoDuel(im)
                xChanging+=3


if __name__ == '__main__':
    main()
