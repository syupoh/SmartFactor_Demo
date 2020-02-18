import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import numpy as np
import os

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
        self.patch_size = 128


        self.window = window12
        self.window.title(window_title)

        self.screen_w = self.window.winfo_screenwidth()
        self.screen_h = self.window.winfo_screenheight()
        self.win_w = int(self.screen_w/6*5)
        self.win_h = int(self.screen_h/2)
        self.win_x = int(80)
        self.win_y = int(30)

        self.main_img_w = int(self.win_w-30)
        self.main_img_h = int(self.win_h/2)

        self.window.geometry("{0}x{1}+{2}+{3}".format(self.win_w, self.win_h, self.win_x, self.win_y))

        ##########################################

        self.n_defect = 3
        self.size_defect = "5 2 3 6 2"
        self.dist_defect = "2 3 1 5 6"

        self.main_img = PIL.Image.open("stitched-leather-texture.jpg")
        detected_img1 = PIL.Image.open("stitched-leather-texture_1.png")
        detected_img2 = PIL.Image.open("stitched-leather-texture_2.jpg")
        detected_img3 = PIL.Image.open("stitched-leather-texture_3.jpg")
        detected_img4 = PIL.Image.open("stitched-leather-texture_4.jpg")
        detected_img5 = PIL.Image.open("stitched-leather-texture_5.jpg")
        
        ##########################################

        self.main_img = self.main_img.resize((self.main_img_w, self.main_img_h))
        self.main_img_tk = PIL.ImageTk.PhotoImage(self.main_img)
        self.main_lbl = tkinter.Label(self.window, image=self.main_img_tk)

        detected_img1 = detected_img1.resize((self.patch_size, self.patch_size))
        detected_img2 = detected_img2.resize((self.patch_size, self.patch_size))
        detected_img3 = detected_img3.resize((self.patch_size, self.patch_size))
        detected_img4 = detected_img4.resize((self.patch_size, self.patch_size))
        detected_img5 = detected_img5.resize((self.patch_size, self.patch_size))

        detected_img1_tk = PIL.ImageTk.PhotoImage(detected_img1)
        detected_img2_tk = PIL.ImageTk.PhotoImage(detected_img2)
        detected_img3_tk = PIL.ImageTk.PhotoImage(detected_img3)
        detected_img4_tk = PIL.ImageTk.PhotoImage(detected_img4)
        detected_img5_tk = PIL.ImageTk.PhotoImage(detected_img5)

        self.detected_lbl1 = tkinter.Label(self.window, image=detected_img1_tk)
        self.detected_lbl2 = tkinter.Label(self.window, image=detected_img2_tk)
        self.detected_lbl3 = tkinter.Label(self.window, image=detected_img3_tk)
        self.detected_lbl4 = tkinter.Label(self.window, image=detected_img4_tk)
        self.detected_lbl5 = tkinter.Label(self.window, image=detected_img5_tk)

        self.label1 = tkinter.Label(self.window, text="defect 갯수 {0}".format(self.n_defect), height=5)
        self.label2 = tkinter.Label(self.window, text="defect 크기 {0}".format(self.size_defect), height=5)
        self.label3 = tkinter.Label(self.window, text="defect 간 거리 {0}".format(self.dist_defect), height=5)

        ##########################################
        # Button that lets the user take a snapshot

        # After it is called once, the update method will be automatically called every delay mill
        self.delay = 100
        self.update()

        self.window.mainloop()

        

    def update(self):

        self.win_w = self.window.winfo_width()
        self.win_h = self.window.winfo_height()

        self.main_img_w = int(self.win_w-30)
        self.main_img_h = int(self.win_h/2)
        self.main_img_x = int((self.win_w - self.main_img_w)/2)
        self.main_img_y = int(10)
        self.patch_y = int(self.win_h - (self.patch_size + 10))  

        if (self.main_img_w > 0 and self.main_img_h >0):
            self.main_img = self.main_img.resize((self.main_img_w, self.main_img_h))
            self.main_img_tk = PIL.ImageTk.PhotoImage(self.main_img)
            self.main_lbl = tkinter.Label(self.window, image=self.main_img_tk)

        self.main_lbl.place(x=self.main_img_x, y=self.main_img_y, width=self.main_img_w, height=self.main_img_h)
        self.detected_lbl1.place(x=self.main_img_x, y=self.patch_y, width=self.patch_size, height=self.patch_size)
        self.detected_lbl2.place(x=self.main_img_x+(self.patch_size+10)*1, y=self.patch_y, width=self.patch_size, height=self.patch_size)
        self.detected_lbl3.place(x=self.main_img_x+(self.patch_size+10)*2, y=self.patch_y, width=self.patch_size, height=self.patch_size)
        self.detected_lbl4.place(x=self.main_img_x+(self.patch_size+10)*3, y=self.patch_y, width=self.patch_size, height=self.patch_size)
        self.detected_lbl5.place(x=self.main_img_x+(self.patch_size+10)*4, y=self.patch_y, width=self.patch_size, height=self.patch_size)


        self.label1.place(x=self.main_img_x+(self.patch_size+10)*5+10, y=self.patch_y, height=13)
        self.label2.place(x=self.main_img_x+(self.patch_size+10)*5+10, y=self.patch_y+(13+5)*1, height=13)
        self.label3.place(x=self.main_img_x+(self.patch_size+10)*5+10, y=self.patch_y+(13+5)*2, height=13)
        self.window.after(self.delay, self.update)


if __name__ == "__main__":
    App(tkinter.Tk(), "Smart Factory Demo")


