import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
img = cv2.imread('images/screen.png',0)
img2 = img.copy()
template = cv2.imread('images/d02.png',0)
w, h = template.shape[::-1]
xcut = 612 + 24 + 60
ycut = 1316 + 59 + 282
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
    plt.savefig('images/searchingImage.png',dpi=760)
    break
sImage = Image.open("images/searchingImage.png")
sImage = sImage.crop((xcut,ycut,xcut2,ycut2))
sImage.save("images/searchingImage.png")
image = Image.open("images/searchingImage.png")
draw = ImageDraw.Draw(image)
draw.ellipse((0,0, 10, 10), fill=(250,235,235,235))
image.save("images/searchingImage.png")
