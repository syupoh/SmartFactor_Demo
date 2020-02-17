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
        patch_size = 128

        self.window = window12
        self.window.title(window_title)
        self.screen_w = self.window.winfo_screenwidth()
        self.screen_h = self.window.winfo_screenheight()
        
        self.win_w = int(self.screen_w/4*3)
        self.win_h = int(self.screen_h/2)
        self.win_x = int(80)
        self.win_y = int(30)
        # self.win_x = int(self.screen_w/10)
        # self.win_y = int(self.screen_h/11)

        main_img_w = int(self.win_w-70)
        main_img_h = int(self.win_h/2)
        main_img_x = int((self.win_w - main_img_w)/2)
        main_img_y = int(10)
        patch_y = int(self.win_h - (patch_size + 10))  
        n_defect = 3
        size_defect = "5 2 3 6 2" 
        dist_defect = "2 3 1 5 6"

        self.window.geometry("{0}x{1}+{2}+{3}".format(self.win_w, self.win_h, self.win_x, self.win_y))

        ##########################################

        main_img = PIL.Image.open("stitched-leather-texture.jpg")
        detected_img1 = PIL.Image.open("stitched-leather-texture_1.png")
        detected_img2 = PIL.Image.open("stitched-leather-texture_2.jpg")
        detected_img3 = PIL.Image.open("stitched-leather-texture_3.jpg")
        detected_img4 = PIL.Image.open("stitched-leather-texture_4.jpg")
        detected_img5 = PIL.Image.open("stitched-leather-texture_5.jpg")
        
        ##########################################

        main_img = main_img.resize((main_img_w, main_img_h))
        detected_img1 = detected_img1.resize((patch_size, patch_size))
        detected_img2 = detected_img2.resize((patch_size, patch_size))
        detected_img3 = detected_img3.resize((patch_size, patch_size))
        detected_img4 = detected_img4.resize((patch_size, patch_size))
        detected_img5 = detected_img5.resize((patch_size, patch_size))

        main_img_tk = PIL.ImageTk.PhotoImage(main_img)
        detected_img1_tk = PIL.ImageTk.PhotoImage(detected_img1)
        detected_img2_tk = PIL.ImageTk.PhotoImage(detected_img2)
        detected_img3_tk = PIL.ImageTk.PhotoImage(detected_img3)
        detected_img4_tk = PIL.ImageTk.PhotoImage(detected_img4)
        detected_img5_tk = PIL.ImageTk.PhotoImage(detected_img5)
        
        label1 = tkinter.Label(self.window, text="defect 갯수 {0}".format(n_defect), height=5)
        label2 = tkinter.Label(self.window, text="defect 크기 {0}".format(size_defect), height=5)
        label3 = tkinter.Label(self.window, text="defect 간 거리 {0}".format(dist_defect), height=5)

        main_lbl = tkinter.Label(self.window, image=main_img_tk)
        detected_lbl1 = tkinter.Label(self.window, image=detected_img1_tk)
        detected_lbl2 = tkinter.Label(self.window, image=detected_img2_tk)
        detected_lbl3 = tkinter.Label(self.window, image=detected_img3_tk)
        detected_lbl4 = tkinter.Label(self.window, image=detected_img4_tk)
        detected_lbl5 = tkinter.Label(self.window, image=detected_img5_tk)

        main_lbl.place(x=main_img_x, y=main_img_y, width=main_img_w, height=main_img_h)
        detected_lbl1.place(x=main_img_x, y=patch_y, width=patch_size, height=patch_size)
        detected_lbl2.place(x=main_img_x+(patch_size+10)*1, y=patch_y, width=patch_size, height=patch_size)
        detected_lbl3.place(x=main_img_x+(patch_size+10)*2, y=patch_y, width=patch_size, height=patch_size)
        detected_lbl4.place(x=main_img_x+(patch_size+10)*3, y=patch_y, width=patch_size, height=patch_size)
        detected_lbl5.place(x=main_img_x+(patch_size+10)*4, y=patch_y, width=patch_size, height=patch_size)
        label1.place(x=main_img_x+(patch_size+10)*5+10, y=patch_y, height=13)
        label2.place(x=main_img_x+(patch_size+10)*5+10, y=patch_y+(13+5)*1, height=13)
        label3.place(x=main_img_x+(patch_size+10)*5+10, y=patch_y+(13+5)*2, height=13)

        ##########################################
        # Button that lets the user take a snapshot

        # After it is called once, the update method will be automatically called every delay mill
        self.delay = 20
        self.update()

        self.window.mainloop()


    def btn_snapshot(self):
        # Get a frame from the video source
        print('btn_sanpshot')
        

    def update(self):

        self.window.after(self.delay, self.update)


if __name__ == "__main__":
    App(tkinter.Tk(), "Smart Factory Demo")


