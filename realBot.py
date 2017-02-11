import pyscreenshot as ImageGrab
import os
import time
import win32api
import win32con
from numpy import *
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw

x1 = 48
y1 = 363

x2 = 173
y1 = 363

x_start = 140
x_end = 480

y_start = 400
y_end = 760

x_difference = 60
y_difference = 282

""" IMAGES """
d1 = "images/d01.png"
d2 = "images/d02.png"
d3 = "images/d03.png"
d4 = "images/d04.png"
d5 = "images/d05.png"
d6 = "images/d06.png"
d7 = "images/d07.png"
d8 = "images/d08.png"
d9 = "images/d09.png"
d10 = "images/d10.png"
d11 = "images/d11.png"
d12 = "images/d12.png"
d13 = "images/d13.png"
d14 = "images/d14.png"
d15 = "images/d15.png"
d16 = "images/d16.png"
d17 = "images/d17.png"
d18 = "images/d18.png"
d19 = "images/d19.png"
d20 = "images/d20.png"
d21 = "images/d21.png"
d22 = "images/d22.png"
d23 = "images/d23.png"
d24 = "images/d24.png"
d25 = "images/d25.png"
d26 = "images/d26.png"
d27 = "images/d27.png"
d28 = "images/d28.png"
d29 = "images/d29.png"
d30 = "images/d30.png"
d31 = "images/d31.png"
d32 = "images/d32.png"
d33 = "images/d33.png"
d34 = "images/d34.png"
d35 = "images/d35.png"
d36 = "images/d36.png"
d37 = "images/d37.png"
d38 = "images/d38.png"
d39 = "images/d39.png"
d40 = "images/d40.png"
d41 = "images/d41.png"
d42 = "images/d42.png"
d43 = "images/d43.png"
d44 = "images/d44.png"
d45 = "images/d45.png"
d46 = "images/d46.png"
d47 = "images/d47.png"
d48 = "images/d48.png"
d49 = "images/d49.png"
d50 = "images/d50.png"
d51 = "images/d51.png"
d52 = "images/d52.png"
d53 = "images/d53.png"
d54 = "images/d54.png"
d55 = "images/d55.png"
d56 = "images/d56.png"
d57 = "images/d57.png"
d58 = "images/d58.png"
d59 = "images/d59.png"

getXYImage = "images/getxy.png"
bonusImage = "images/bonus.png"
screen = "images/screen.png"
duelImage = "images/duel.png"
nextImage = "images/next.png"
okImage = "images/ok.png"
autoDuelImage = "images/autoduel.png"
skipImage = "images/skip.png"
backImage = "images/back.png"
towerImage = "images/tower.png"
searchingImage = "images/searchingImage.png"

duelists = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11,
            d12, d13, d14, d15, d16, d17, d18, d19, d20, d21,
            d22, d23, d24, d25, d26, d27, d28, d29, d30, d31,
            d32, d33, d34, d35, d36, d37, d38, d39, d40, d41,
            d42, d43, d44, d45, d46, d47, d48, d49, d50, d51,
            d52, d53, d54, d55, d56, d57, d58, d59]
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
        time.sleep(0.002)
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

def searchXY():
    x,y = locateImage(screen,getXYImage)
    if x != 1:
        print ("GOT XY")
        print (x,y)
        return x,y
    return 0,0

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

def searchTower():
    x,y = locateImage(screen,towerImage)
    if x != 1:
        print ("TOWER")
        return True
    return False

def searchDuelist(xWind,yWind):
    # Processo lento para procurar duelistas
    for duelist in duelists:
        bestLocateImage(duelist, xWind,yWind)
        x,y = searchBrightness()
        if x != 1:
            leftClick(x+xWind+x_difference,y+yWind+y_difference)
            print ("DUELIST")
            print (duelist)
            return True
        print ("TRYING")
    return False

def oldSearchDuelist():
    # Processo rápido para procurar duelistas
    for duelist in duelists:
        x,y = locateImage(screen,duelist)
        if x != 1:
            leftClick(x,y)
            print ("DUELIST")
            return True
    return False

def locateImage(fullImage, partImage):
    # Retorna as coordenadas da partImage dentro da fullimage
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

def bestLocateImage(duelist,xWind, yWind):
    img = cv2.imread(screen,0)
    img2 = img.copy()
    template = cv2.imread(duelist,0)
    w, h = template.shape[::-1]
    xcut = 612 + xWind + 60
    ycut = 1316 + yWind + 282
    xcut2 = xcut + 419
    ycut2 = ycut + 516
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
         top_left = min_loc
        else:
         top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img,top_left, bottom_right, 255, 2)

        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.savefig(searchingImage,dpi=760)
        break
    # Corta a imagem para diminuir processamento
    sImage = Image.open(searchingImage)
    sImage = sImage.crop((xcut,ycut,xcut2,ycut2))
    sImage.save(searchingImage)
    # Desenha na imagem um círculo brilhoso para evitar bugs
    image = Image.open(searchingImage)
    draw = ImageDraw.Draw(image)
    draw.ellipse((0,0, 10, 10), fill=(250,235,235,235))
    image.save(searchingImage)

def searchBrightness():
    # Acha o ponto mais brilhante de uma imagem
    image = cv2.imread(searchingImage)
    orig = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    image = orig.copy()
    cv2.circle(image, maxLoc, 15, (255, 0, 0), 2)
    # Verifica se não é o ponto previamente colocado para evitar bugs
    # Verifica se não é o trader brilhando
    if maxLoc[0] > 10:
        if searchTower() and maxLoc[0] >= 120 and maxLoc[0] <= 277 and maxLoc[1] >= 359 and maxLoc[1] <= 500:
            return 1,1
        else:
            return maxLoc[0], maxLoc[1]
    else:
        # Retorna 1,1 caso não ache ninguém
        return 1,1

def main():
    # Todo screenSHot() atualiza a imagem screen
    # Inicializa o searches e o start
    searches = 0
    start = True
    time.sleep(3)
    while(True):
        # Se estiver indo para a 11 volta (5 lentas) reseta o searches
        if searches >= 10:
            searches = 0
        # Procura o X,Y da parte superior esquerda do app
        while start:
            screenShot()
            xWind,yWind = searchXY()
            if xWind != 0:
                start = False
        start = True
        screenShot()
        # Se deu 5 voltas rapidas, começa as lentas
        if searches >= 5:
            # Processo lento para achar o duelista e duelar
            if searchDuelist(xWind,yWind):
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
                    elif searchOk():
                        pass
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
                        searches = 0
            else:
                searches += 1
                searchBack()
                slideLeft()
        # Se não fez as 5 rápidas, continua nelas
        else:
            # Processo para achar o duelista e duelar
            if oldSearchDuelist():
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
                    elif searchOk():
                        pass
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
                        searches = 0
            else:
                searches += 1
                searchBack()
                slideLeft()

if __name__ == '__main__':
    main()
