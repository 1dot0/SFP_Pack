
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import socket
import cv2
from PIL import Image, ImageTk
import subprocess
import time
import threading
import platform
import numpy as np
import psutil

STOPVIDEO = False
PAUSEVIDEO = False
FOLDERWITHVIDEOS = "C:/Users/leona/OneDrive/Documenti/Programmazione/Hacking/FaceItAloneVideos/"
TARGETVIDEO = ""
SOURCEVIDEO = FOLDERWITHVIDEOS

root = tk.Tk()
root.title("SFP_Queen")
root.geometry("1280x720")

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text = "Toxicity")
tab_control.add(tab3, text= "Mercury")
tab_control.add(tab2, text = "Face It Alone")

def tab1_making(parent):
    pass

def tab3_making(parent):
    pass

def tab2_making(parent):
    nameLBL = Label(tab2, text="Face It Alone", font=("Arial", 17))
    nameLBL.pack()

    streaNameLBL = Label(tab2, text="NO VIDEO INPUT", font=("Arial", 7))
    streaNameLBL.place(x=0,y=13)

    coverImage = Canvas(tab2, width=640, height=360, bg="Black")
    coverImage.place(x=0,y=30)

    logText = Canvas(tab2, width=1280, height=30, bg="Black")
    logText.place(x=0, y=660)

    def startButton():
        global STOPVIDEO
        global PAUSEVIDEO
        video = SOURCEVIDEO
        
        streaNameLBL.config(text=TARGETVIDEO)
        #Initialize video reader
        cap = cv2.VideoCapture(video)

        #creates a label to visualize the video
        videoPlayer = tk.Label(tab2)
        videoPlayer.place(x=0, y=30)

        #Starts reproducing video
        while True:
            if not PAUSEVIDEO:
                ret, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 360))
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            videoPlayer.config(image=img)    
            root.update()
            
            if STOPVIDEO == True:
                STOPVIDEO = False
                break
            
        #releases recurses
        cap.release()
        coverImage = Canvas(tab2, width=640, height=360, bg="Black")
        coverImage.place(x=0,y=30)
        streaNameLBL.config(text="NO VIDEO INPUT")
    startButton = Button(tab2, text="Start", command=startButton, padx=20, pady=10)
    startButton.place(x=0, y=400)

    def stopButton():
        global STOPVIDEO
        STOPVIDEO = True
    stopButton = Button(tab2, text="Stop", command=stopButton, padx=20, pady=10)
    stopButton.place(x=70, y=400)

    def liveThreadf():
        global STOPVIDEO
        print("Thread Start")

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', 12345))
        serversocket.listen(5)
        while True:
            clientsocket, addr = serversocket.accept()
            print("Got Connected to")
            videoPlayer = tk.Canvas(tab2, height=360, width=640, bg="Blue")
            videoPlayer.place(x=0, y=30)
            while True: #si impalla in questo ciclo senza fare nulla
                data = clientsocket.recv(4096)
                print(data)
                if not data or STOPVIDEO == True:
                    STOPVIDEO = False
                    break
            frame = cv2.imdecode(np.fromstring(data, np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow("Video", img)
            cv2.waitKey(1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 360))
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            videoPlayer.config(image=img)
            root.update()
                
            if STOPVIDEO == True:
                STOPVIDEO = False
                break
        clientsocket.close()
        print("Thread Stop")

    def liveButton():
        #Launches SFP_FaceItAlone.txt on one of the hosts saved in SFP_Mercury wich has the program on it
        #shows what it is recording
        #writes the name of the host it is currently running on over the video player.
        #when turned off the name turns to normal



        subprocess.run(["python", "SFP_FaceItAlone.py"])
        streaNameLBL.config(text=platform.node())
        liveThread = threading.Thread(target=liveThreadf)
        liveThread.start()
    liveButton = Button(tab2, text="Live", command=liveButton, padx=20, pady=10)
    liveButton.place(x=140, y=400)

    def pauseButton():
        global PAUSEVIDEO
        PAUSEVIDEO = not PAUSEVIDEO
    pauseButton = Button(tab2, text="Pause/Restart", command=pauseButton, padx=20, pady=10)
    pauseButton.place(x=205, y=400)
    
    fileListLbl = Label(tab2, text="Lista Video: ")
    fileListLbl.place(x=650, y=30)
    def on_select(event):
        global SOURCEVIDEO
        global TARGETVIDEO
        index = videoList.curselection()[0]
        TARGETVIDEO = videoList.get(index)
        SOURCEVIDEO = FOLDERWITHVIDEOS + TARGETVIDEO
    filenames = []
    for file in os.listdir(FOLDERWITHVIDEOS):
        if os.path.isfile(os.path.join(FOLDERWITHVIDEOS, file)):
            filenames.append(file)
    videoList = tk.Listbox(tab2)
    for file in filenames:
        videoList.insert(tk.END, file)
    videoList.config(width=30, height=21)
    videoList.bind("<<ListboxSelect>>", on_select)
    videoList.place(x=650, y=50)

    def rename():
        global TARGETVIDEO
        global SOURCEVIDEO
        global FOLDERWITHVIDEOS
        if TARGETVIDEO != "":
            newName = renameEntry.get() + ".avi"
            os.rename(SOURCEVIDEO, FOLDERWITHVIDEOS + newName)
        root.update()
        videoList.update()
    renameEntry = Entry(tab2)
    renameEntry.config(width=27)
    renameEntry.place(x=656, y=390)
    renameButt = Button(tab2, text="Rename", command=rename, padx=18, pady=5)
    renameButt.place(x=655, y=405)
    def delete():
        global TARGETVIDEO
        global SOURCEVIDEO
        if TARGETVIDEO != "":
                os.remove(SOURCEVIDEO)
                TARGETVIDEO = ""
                SOURCEVIDEO = FOLDERWITHVIDEOS + TARGETVIDEO
    deleteButt = Button(tab2, text="Delete",command=delete, padx=18, pady=5)
    deleteButt.place(x=745,y=405)

tab1_making(root)
tab3_making(root)
tab2_making(root)
tab_control.pack(expand = 1, fill = 'both')

root.mainloop()