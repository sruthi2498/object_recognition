from PIL import Image
import pytesseract
import argparse
import cv2
import os
import sys
from pytesseract import *

image=cv2.imread(sys.argv[1])


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

ret,gray = cv2.threshold(gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
gray2 = cv2.medianBlur(gray1, 3)



filename = "new_op_1.png"
cv2.imwrite(filename, gray)

filename2 = "new_op_2.png"
cv2.imwrite(filename2, gray2)

im=Image.open(filename)

text = pytesseract.image_to_string(im)
os.remove(filename)
print "ok"
print(text)
 
# show the output images
cv2.imshow("Output", gray)
cv2.waitKey(0)

im2=Image.open(filename2)

text2 = pytesseract.image_to_string(im2)
os.remove(filename2)
print "ok"
print(text2)
 
# show the output images
cv2.imshow("Output", gray2)
cv2.waitKey(0)