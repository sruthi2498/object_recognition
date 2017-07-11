
import cv2
import sys
#import extract_text
'''opencv_createsamples -num 117 -vec object.vec -info data/pos/annotations.txt -bg bg.txt
opencv_traincascade  -featureType LBP -w 24 -h 24 -numPos 99 -data data -bg bg.txt -acceptanceRatioBreakValue 0.00001 
    -vec object.vec '''


cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
t=1
while(t):
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print gray
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(22, 22),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if(len(faces)>0):
        t=0
    #print faces
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        crop_img = gray[y:y+h, x:x+w] # Crop from x, y, w, h -> 100, 200, 300, 400
        cv2.imshow('cropped',crop_img)
        cv2.waitKey(0)
        cv2.imwrite('op.png',crop_img)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if(t==0):
        cv2.waitKey(0)

# When everything is done, release the capture
'''video_capture.release()
cv2.destroyAllWindows()'''