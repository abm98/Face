import cv2
from random import randrange
#load some pre trained data on face frontal from opencv_storage(haar cascade algorithms)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose image to detect face
#img = cv2.imread('Beard.jpg')
# To detect image from webcam
webcam = cv2.VideoCapture('kyatum.mp4')  # if argument is given as 0 it will run through your webcam otherwise as per given file in quote

# Iterate forever over frame
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()


#Convert to Grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Detect face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
                    #(grayscaled_img,2,6) you can change the value to change senstivity of detection
# Draw rectangle around face
    for (x, y, w, h) in face_coordinates:
    # (0,0,0) change for color / ,4) change thickness
        cv2.rectangle(frame,(x,y),(x+w, y+h), (randrange(255),randrange(255),randrange(255)),4)

 # if you are using single image and there is multiple pic change the array value and rectangle will replace to next image
 # (x,y,w,h) = face_coordinates[0]
 # print(face_coordinates)

#Display the images with faces
# for running the program only for image change the **** frame to img
    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)
    # STOP if Q(81/113 ASCII) key is pressed
    if key == 81 or key ==113:
        break
# Release the video object which is capture
webcam.release()



print("Masood")
