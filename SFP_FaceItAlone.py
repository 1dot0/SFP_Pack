"""
Face it Alone is a software wich can be controlled by SFP_Queen.
It's purpose is to open the webcam connected to the pc it is on, sending live frame by frame everything it is recording to be 
displayed by Queen and also to record a video which it will be saved in a target directory, which can be also read by Queen.
"""

import cv2
import os
import platform

FOLDER = "FaceItAloneVideos"
RUNNINGDEVICE = platform.node()
FILENAME = RUNNINGDEVICE+" - "+str(len(os.listdir(FOLDER)))+".avi"
KEEPRUNNING = True

#creates a videocapture
capture = cv2.VideoCapture(0)

#gives error if camera does not open properly
if not capture.isOpened():
    print("NO VIDEO INPUT")

#Sets how big the frame will be
frameW = int(capture.get(3))
frameH = int(capture.get(4))

#Starts recording the video
video = cv2.VideoWriter(FOLDER + "/" + FILENAME, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frameW, frameH))

while True:
    keep, camera = capture.read()
    if keep == True:

        #adds frames to the video
        video.write(camera)

        #shows camera output
        cv2.imshow(RUNNINGDEVICE, camera)

        if not KEEPRUNNING:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #breaks loop
    else:
        break

#releases everything
video.release()
capture.release()

#close window
cv2.destroyAllWindows()
