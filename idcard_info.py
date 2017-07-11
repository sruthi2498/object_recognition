from __future__ import division
import cv
import cv2
import sys
import numpy as np
import copy
import os
#fpath=os.path.join("data/pos", "annotations.txt")

fpath=os.path.join("data", "cascade.xml")

'''
if len(sys.argv) < 2:
	print "Usage: ", sys.argv[0], " <image filename>"
	sys.exit()

def cv_size(img):
    return tuple(img.shape[1::-1])
# Load image and split into RGB planes
n=len(sys.argv)
for i in range(1,n):
	image=cv2.imread(sys.argv[i])
	print "Loaded"
	cv2.imshow("image",image);
	cv2.waitKey(0)
'''
# opencv_createsamples -num 117 -vec object.vec -info data/pos/annotations.txt -bg bg.txt
#opencv_traincascade  -featureType LBP -w 24 -h 24 -numPos 99 -data data -bg bg.txt -acceptanceRatioBreakValue 0.00001 -vec object.vec 
print sys.argv[0]
print sys.argv[1]

n=len(sys.argv)
for i in range(1,n):
	image=cv2.imread(sys.argv[i])
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	filename=fpath
	detector=cv2.CascadeClassifier(filename)
	print "detector",detector
	print detector.empty()
	print "detector.getFeatureType()",detector.getFeatureType()
	rects = detector.detectMultiScale(gray,maxSize=(80,100))
	print "rects ",rects
	for (i, (x, y, w, h)) in enumerate(rects):
		print "ok"
		cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)
	 
	
	cv2.imshow("image", image)
	cv2.waitKey(0)