# import library

from PIL import Image
import numpy as np


def BGR2GRAY(img):

    for y in range (height):
        for x in range (width):        
            R=img[y,x,0]
            G=img[y,x,1]
            B=img[y,x,2]

            Y = 0.2126*R + 0.7152*G + 0.0722*B
            img[y,x,0:3]=Y

    
    out=img
    
    return out
    

def binalization(img, th=128):

    for y in range (height):
        for x in range (width):

            if img[y,x,0] >= th:
                img[y,x,0:3]=255
            else:
                img[y,x,0:3]=0
    
    return img

# 이미지 불러오기
Img = Image.open('Audrey.png')
width, height = Img.size
result = np.array((Img),dtype=float)

##### do not edit here #####
result = BGR2GRAY(result)
result = binalization(result)
result = Image.fromarray(result.astype('uint8'))
result.save('./result.png')





