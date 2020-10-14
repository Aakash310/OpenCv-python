import cv2
import numpy as np
from matplotlib import pyplot as plt

def region_of_interest(img , vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask , vertices , match_mask_color)
    masked_image = cv2.bitwise_and(img , mask)
    return masked_image

def draw_the_lines(img ,lines):
    image = np.copy(img)
    blank_image = np.zeros((image.shape[0],image.shape[1],3 ), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line( image , (x1,y1) , (x2,y2) , (0,255,0) , 3)

    image = cv2.addWeighted(image , 0.8 , blank_image , 1 , 0.0) 
    return image       

img = cv2.imread('Road.png')
img = cv2.resize( img , (1279,704))
img = cv2.cvtColor( img , cv2.COLOR_BGR2RGB)

print(img.shape)
height = img.shape[0]
width = img.shape[1]

region_of_interest_vertices = [(0,height) , (width/2,height/5) , (width,height)]

gray_image = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)  
canny_image = cv2.Canny(gray_image,100,200)
cropped_image = region_of_interest(canny_image , np.array([region_of_interest_vertices],np.int32)) 

lines = cv2.HoughLinesP( cropped_image , rho = 6 , theta = np.pi/60 , threshold = 160 , lines= np.array([]) , minLineLength= 40 , maxLineGap= 25)

image_with_lines = draw_the_lines(img , lines)

plt.imshow(image_with_lines)
plt.show()
cv2.destroyAllWindows()