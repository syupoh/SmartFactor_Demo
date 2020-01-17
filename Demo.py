import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import numpy as np


def detectionalgo(inimg):
    fullimg = inimg.copy()
    pix = 32
    bins = 16
    sz = fullimg.shape
    lh = sz[0]
    lw = sz[1]

    Dist = np.zeros((int(lh / pix) * int(lw / pix), bins, 3))

    for y in range(int(lh / pix)):
        for x in range(int(lw / pix)):
            current = fullimg[(y) * pix:(y + 1) * pix, (x) * pix:(x + 1) * pix]
            rectimg = fullimg.copy()

            ### calculate histogram
            hist1 = cv2.calcHist([current], [0], None, [bins], [0, 256])  ## B
            hist2 = cv2.calcHist([current], [1], None, [bins], [0, 256])  ## G
            hist3 = cv2.calcHist([current], [2], None, [bins], [0, 256])  ## R

            hist1.resize(bins)
            hist2.resize(bins)
            hist3.resize(bins)
            Dist[x + y * int(lw / pix), :, 0] = hist1
            Dist[x + y * int(lw / pix), :, 1] = hist2
            Dist[x + y * int(lw / pix), :, 2] = hist3

    meandis = np.mean(Dist, axis=0)
    for y in range(int(lh / pix)):
        for x in range(int(lw / pix)):
            AB = np.abs(Dist[x + (y) * (int(lw / pix)), :, :] - meandis)

            for index, item in enumerate(AB):
                if item[0] == 0:
                    AB[index][0] = 1
                if item[1] == 0:
                    AB[index][1] = 1
                if item[2] == 0:
                    AB[index][2] = 1

            ABC = np.log(AB)

            measuredist = np.mean(np.mean(ABC, axis=1), axis=0)

            # print(measuredist)
            if measuredist > 0.9:
                cv2.rectangle(fullimg, ((x) * pix, (y) * pix), ((x + 1) * pix, (y + 1) * pix), (0, 255, 0), 2)

    return fullimg


def windowopen(name, size):
    window = tkinter.Tk()
    window.title(name)
    window.geometry(size)
    window.resizable(False, False)
    return window


class App:
    def __init__(self, window12, window_title, video_source="C:/Users/JOHN/Downloads/FabricVideo.mp4"):
        self.capsz = 250
        self.butsz = 200

        # open video source (by default this will try to open the computer webcam)
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)

        self.window = window12
        self.window.title(window_title)
        self.window.geometry("{0}x{1}+{2}+{3}".format(int(self.vid.width*2+self.butsz), int(self.vid.height),
                             int(self.vid.width * 1 / 10),int(self.vid.height*1/10)))

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self.window, width=self.vid.width*2+self.butsz, height=self.vid.height)
        self.canvas.pack(side="left")

        # Button that lets the user take a snapshot
        self.btn_snapshot = tkinter.Button(self.window, overrelief="solid",
                                           text="Detect", width=self.butsz, command=self.snapshot)
        self.btn_snapshot.place(x=self.vid.width, y=0,
                                height=self.vid.height, width=self.vid.width*1/7)

        # After it is called once, the update method will be automatically called every delay mill
        self.delay = 20
        self.update()

        self.window.mainloop()


    def snapshot(self):
        # Get a frame from the video source

        ret, self.img, self.ori_width, self.ori_height = self.vid.get_frame()

##################################

        # Algorithm for detection

        self.capture = self.img[int(self.vid.height // 2 - (self.capsz // 2)):int(self.vid.height // 2 + (self.capsz // 2)),
                       int(self.vid.width // 2 - (self.capsz // 2)):int(self.vid.width // 2 + (self.capsz // 2))]
        self.result = detectionalgo(self.capture)

        # lt = detectionalgo(self.capture[0:int(self.capsz/2), 0:int(self.capsz/2)])
        # rt = detectionalgo(self.capture[0:int(self.capsz/2), int(self.capsz/2):int(self.capsz)])
        # lb = detectionalgo(self.capture[int(self.capsz/2):int(self.capsz), 0:int(self.capsz/2)])
        # rb = detectionalgo(self.capture[int(self.capsz/2):int(self.capsz), int(self.capsz/2):int(self.capsz)])

##################################

        self.render1 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.img))

        # self.render2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(lt))
        # self.render3 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(rt))
        # self.render4 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(lb))
        # self.render5 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(rb))

        self.render6 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.result))

        offset = self.vid.width+self.butsz-10


        self.canvas.create_image(int(offset), 0, image=self.render1, anchor=tkinter.NW)

        # #lt
        # self.canvas.create_image(int(offset + self.vid.width // 2 - (self.capsz // 2))
        #                          , int(self.vid.height // 2 - (self.capsz // 2))
        #                          , image=self.render2, anchor=tkinter.NW)
        #
        # #rt
        # self.canvas.create_image(int(offset + self.vid.width // 2)
        #
        #                          , int(self.vid.height // 2 - (self.capsz // 2))
        #                          , image=self.render3, anchor=tkinter.NW)
        #
        # #lb
        # self.canvas.create_image(int(offset + self.vid.width // 2 - (self.capsz // 2))
        #                          , int(self.vid.height // 2)
        #                          , image=self.render4, anchor=tkinter.NW)
        #
        # #rb
        # self.canvas.create_image(int(offset + self.vid.width // 2)
        #                          , int(self.vid.height // 2)
        #                          , image=self.render5, anchor=tkinter.NW)

        self.canvas.create_image(int(offset + self.vid.width // 2 - (self.capsz // 2))
                                 , int(self.vid.height // 2  - (self.capsz // 2))
                                 , image=self.render6, anchor=tkinter.NW)


        self.canvas.create_rectangle(offset + self.vid.width // 2 - (self.capsz // 2),
                                     self.vid.height // 2 - (self.capsz // 2),
                                     offset + self.vid.width // 2 + (self.capsz // 2),
                                     self.vid.height // 2 + (self.capsz // 2),
                                     outline='yellow', width=3)

        # cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        ret, frame, self.ori_width, self.ori_height = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            self.canvas.create_rectangle(self.vid.width // 2 - (self.capsz // 2), self.vid.height // 2 - (self.capsz // 2),
                                         self.vid.width // 2 + (self.capsz // 2), self.vid.height // 2 + (self.capsz // 2),
                                         outline='yellow', width=3)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source='rainy.avi'):
#########################
        self.vid = cv2.VideoCapture(0)
        # self.vid = cv2.VideoCapture(video_source)

###############################
        if not self.vid.isOpened():
           raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)


    def get_frame(self):
        ret, frame = self.vid.read()
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                return (ret, frame, self.width, self.height)
            else:
                self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
                return (ret, None, self.width, self.height)
        else:
            #self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            #ret, frame = self.vid.read()
            #return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            return (ret, None, self.width, self.height)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


App(tkinter.Tk(), "Smart Factory Demo")
