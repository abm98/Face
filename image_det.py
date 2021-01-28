import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Beard.jpg')

#Convert to Grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangle around face
for (x, y, w, h) in face_coordinates:
    # (0,0,0) change for color / ,4) change thickness
    cv2.rectangle(img,(x,y),(x+h, y+w), (randrange(255),randrange(255),randrange(255)),4)
cv2.imshow('ABM Face Detector', img)
cv2.waitKey()
print(face_coordinates)
print("Mas")
