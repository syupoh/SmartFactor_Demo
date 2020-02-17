import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import numpy as np

def windowopen(name, size):
    window = tkinter.Tk()
    window.title(name)
    window.geometry(size)
    window.resizable(False, False)
    return window


class App:
    def __init__(self, window12, window_title):
        self.capsz = 250
        self.butsz = 200

        # open video source (by default this will try to open the computer webcam)
        # self.video_source = video_source
        # self.vid = MyVideoCapture(self.video_source)

        self.window = window12
        self.window.title(window_title)
        self.screen_w = tkinter.Tk().winfo_screenwidth()
        self.screen_h = tkinter.Tk().winfo_screenheight()

        width = self.screen_w/2
        height = self.screen_h/2
        self.window.geometry("{0}x{1}+100+50".format(int(width), int(height)))

        # Button that lets the user take a snapshot
        self.btn_snapshot = tkinter.Button(self.window, overrelief="solid",
                                           text="Detect", width=self.butsz, command=self.btn_snapshot)

        # self.canvas3 = tkinter.Canvas(self.window, width=self.vid.width, height=self.vid.height)
        
        # After it is called once, the update method will be automatically called every delay mill
        self.delay = 20
        self.update()

        self.window.mainloop()


    def btn_snapshot(self):
        # Get a frame from the video source
        print('btn_sanpshot')
        

    def update(self):

        self.window.after(self.delay, self.update)



App(tkinter.Tk(), "Smart Factory Demo")


