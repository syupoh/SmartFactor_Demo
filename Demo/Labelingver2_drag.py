from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

import os
import time
import numpy as np

class ImageEditor(Frame):
    def __init__(self,root):
        """Initializes the window with access to an imagefeed class that supplies from and saves images to the appropriate locations"""
        self.swit = 0

        self.imgdirlist = ''

        self.winh = 200 
        self.winw = 400
        self.xoffset = 50
        self.yoffset = 30
        self.colorcode = [[0,0,0],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255] 
        ,[255,255,255]]
        self.colorname = ['black', 'red', 'green', 'blue', 'yellow', 'skyblue', 'magenta'
        , 'white']

###############################
        xoffset = self.xoffset
        yoffset = self.yoffset


        root.geometry("%dx%d+200+100"%(self.winw,self.winh))
        root.resizable(False, False)

        ##### Components generate
        self.C = Canvas(root, width=self.winw, height=self.winh,bd=0, highlightthickness=0)
        self.C.pack()

        self.lbl1 = Label(root, text='width')
        self.lbl2 = Label(root, text='height')
        self.lbl3 = Label(root, text='type')
        self.lbl4 = Label(root, text='red')
        self.txt1 = Entry(root,width=10)
        self.txt2 = Entry(root,width=10)
        self.txt3 = Entry(root,width=5)

        self.butt = Button(root, overrelief="solid",
                               text='Rectangle',
                               command=self.buttrec, repeatdelay=1000, repeatinterval=100)
        self.butt2 = Button(root, overrelief="solid",
                        text='Reset',
                        command=self.buttreset, repeatdelay=1000, repeatinterval=100)
        
        self.butt3 = Button(root, overrelief="solid",
                               text='Labeling',
                               command=self.buttlabel, repeatdelay=1000, repeatinterval=100)
                               
        self.butt_file = Button(root, overrelief="solid",
                               text='FileLoad',
                               command=self.buttfile, repeatdelay=1000, repeatinterval=100)
                               
        self.butt_dir = Button(root, overrelief="solid",
                               text='Directory Load',
                               command=self.buttdir, repeatdelay=1000, repeatinterval=100)
        
        ##### Components place
        self.lbl1.place(y=yoffset+20, x=xoffset+10)
        self.lbl2.place(y=yoffset+40, x=xoffset+10)
        self.lbl3.place(y=yoffset+20, x=xoffset+170)
        self.lbl4.place(y=yoffset+20, x=xoffset+240)
        
        self.txt1.place(y=yoffset+20, x=xoffset+50)
        self.txt2.place(y=yoffset+40, x=xoffset+50)
        self.txt3.place(y=yoffset+20, x=xoffset+200)

        self.butt.place(y=yoffset+60, x=xoffset+150, height=30, width=75)
        self.butt2.place(y=yoffset+60, x=xoffset+225, height=30, width=75)
        self.butt3.place(y=yoffset+90, x=xoffset+150, height=30, width=150)
        self.butt_file.place(y=yoffset-20, x=xoffset+120, height=30, width=100)
        self.butt_dir.place(y=yoffset-20, x=xoffset, height=30, width=120)

        self.txt1.insert(0,'10')
        self.txt2.insert(0,'10')
        self.txt3.insert(0,1)
        
        ########################## get the variables on Entry
        self.root = root

        self.framew = int(self.txt1.get())
        self.frameh = int(self.txt2.get())
        self.framet = int(self.txt3.get())
        # self.buttrec()
        
        self.lbl4.configure(text=self.colorname[self.framet])
        
        self.lbl5y= self.yoffset+80
        self.lbl5x= self.xoffset-10
        self.lbl5 = Label(self.root, text='(%d x %d)'%(int(self.framew),int(self.frameh)))
        self.lbl5.place(y=self.lbl5y, x=self.lbl5x)
        self.rectx = self.lbl5x + 90 - self.framew/2
        self.recty = self.lbl5y + 10 - self.frameh/2
        self.rect = self.C.create_rectangle(self.rectx,self.recty,self.rectx+self.framew,self.recty+self.frameh)
        ################################
        # self.initUI()
        self.root.mainloop()  


    def buttrec(self):
        ########################### get the variables on Entry
        self.framew = int(self.txt1.get())
        self.frameh = int(self.txt2.get())
        self.framet = int(self.txt3.get())
        ###############################################
        self.C.delete(self.rect)
        self.lbl5.destroy()

        self.lbl5 = Label(self.root, text='(%d x %d)'%(int(self.framew),int(self.frameh)))
        self.lbl5.place(y=self.lbl5y, x=self.lbl5x)
        
        self.rect = self.C.create_rectangle(self.rectx,self.recty,self.rectx+self.framew,self.recty+self.frameh)
        
        self.lbl4.configure(text=self.colorname[self.framet])
        
    
        ########################### Load the image
    def buttfile(self):
        self.imgdir =  filedialog.askopenfilename(initialdir = os.getcwd(),
        title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        # self.imgdir = '/media/syup/Seagate_1TB/python/Remote/_mine/SmartFactory/datatemp/def_5_76_29_22_20171127_173147.jpg'

#########################
        self.img = ImageTk.PhotoImage(Image.open(self.imgdir))

        self.window2 = Toplevel()
        self.window2.title("Image")
        self.window2.geometry("%dx%d+700+100"%(self.img.width(),self.img.height()))
        self.C2 = Canvas(self.window2, width=self.img.width(), height=self.img.height(),bd=0, highlightthickness=0)
        self.C2.pack()
        self.C2.create_image(0,0,anchor="nw",image=self.img)


        self.outimg = np.zeros([self.img.height(), self.img.width(),3])
        outim = ImageTk.PhotoImage(Image.fromarray(np.uint8(self.outimg)))
        
        self.window3 = Toplevel()
        self.window3.title("GroundTruth")
        self.window3.geometry("%dx%d+700+500"%(self.img.width(),self.img.height()))
        self.C3 = Canvas(self.window3, width=self.img.width(), height=self.img.height(),bd=0, highlightthickness=0)
        self.C3.pack()
        self.C3.create_image(0, 0, anchor="nw",image=outim)
##########################

        self.imgdirlist = ''
        self.initUI()

    def buttdir(self):               
        # self.FilePath = filedialog.askdirectory(title = "Directory selection",
        #  initialdir=os.path.dirname(os.getcwd()), mustexist = True)
         
         
        if not os.path.exists('/media/'):
            self.FilePath = "~/Dropbox/"
            self.FilePath = "/media/syup/Toshiba_3TB/Dropbox/"
        else:
            self.FilePath = "C:/Users/JOHN/Dropbox/"
        self.FilePath = self.FilePath + "_ISPL/SmartFactory/Seam_work_full/190121_stitch_yup_half2/1"

        # self.FilePath = self.FilePath + 
        # self.FilePath = '/media/syup/Toshiba_3TB/SmartFactory/181004_BusinessTrip/Seam_work_half/1/'
        # self.FilePath = "/media/syup/Seagate_1TB/python/Remote/_mine/SmartFactory/datatemp"
        # self.FilePath = "C:/Users/JOHN/Dropbox/_ISPL/SmartFactory/Seam_work_half2/2/"

        included_extenstions = ['jpg', 'bmp', 'png', 'gif']
        self.imgdirlist = [fn for fn in os.listdir(self.FilePath)
                    if any(fn.endswith(ext) for ext in included_extenstions)]
            
        self.dirn = 0

        # print(self.FilePath)
        # print(self.imgdirlist)
        # print(len(self.imgdirlist))
        # print(self.imgdir)

        self.imgdir = self.FilePath+'/'+self.imgdirlist[self.dirn]
        self.img = ImageTk.PhotoImage(Image.open(self.imgdir))

        self.window2 = Toplevel()
        self.window2.title("Image")
        self.window2.geometry("%dx%d+700+100"%(self.img.width(),self.img.height()))
        self.C2 = Canvas(self.window2, width=self.img.width(), height=self.img.height(),bd=0, highlightthickness=0)
        self.C2.pack()
        self.C2.create_image(0,0,anchor="nw",image=self.img)

        self.outimg = np.zeros([self.img.height(), self.img.width(),3])
        outim = ImageTk.PhotoImage(Image.fromarray(np.uint8(self.outimg)))
        
        self.window3 = Toplevel()
        self.window3.title("GroundTruth")
        self.window3.geometry("%dx%d+700+500"%(self.img.width(),self.img.height()))
    

        self.C3 = Canvas(self.window3, width=self.img.width(), height=self.img.height(),bd=0, highlightthickness=0)
        self.C3.pack()
        self.C3.create_image(0,0,anchor="nw",image=outim)

        self.initUI()


        ########################### Save the labeled image
    def buttlabel(self):
        # self.FilePath = os.path.dirname(
        #         os.path.realpath(self.imgdir)
        #         )    
        self.FileName = (os.path.basename(self.imgdir))
        
        if not os.path.exists(self.FilePath+'/GroundTruth/'):
            os.mkdir(self.FilePath+'/GroundTruth/')
            
        Tgt = self.FilePath+'/didit/'       

        if not os.path.exists(Tgt):
            os.mkdir(Tgt)
    
        outim = Image.fromarray(np.uint8(self.outimg))

        print('File Saved at :')
        print(' '+self.FilePath+'/GroundTruth/'+self.FileName)
        outim.save(self.FilePath+'/GroundTruth/'+self.FileName)

        os.rename(self.FilePath+self.FileName, Tgt+self.FileName)

        if not self.imgdirlist == '':
            if self.dirn+1 == len(self.imgdirlist):
                messagebox.showinfo("End", "There are no more files left.")
            else:
                self.dirn = self.dirn + 1
                self.imgdir = self.FilePath+'/'+self.imgdirlist[self.dirn]
                
                self.img = ImageTk.PhotoImage(Image.open(self.imgdir))
                self.outimg = np.zeros([self.img.height(), self.img.width(),3])
                outim = ImageTk.PhotoImage(Image.fromarray(np.uint8(self.outimg)))

                self.C2.delete('all')
                self.C3.delete('all')
                self.C2.create_image(0,0,anchor="nw",image=self.img)
                self.C3.create_image(0,0,anchor="nw",image=outim)
                self.window3.mainloop()  
                


        self.initUI()
    
        ########################### Reset rectangles
    def buttreset(self):
        self.C2.delete("all")
        self.C2.create_image(0,0,anchor="nw",image=self.img)
        
        self.outimg = np.zeros([self.img.height(), self.img.width(),3])
        outim = ImageTk.PhotoImage(Image.fromarray(np.uint8(self.outimg)))

        self.C3.create_image(0,0,anchor="nw",image=outim)
        
        self.initUI()
     
    
        ########################### Update the example rectangle
    def initUI(self):
        self.C2.bind("<Enter>", self.on_enter)
        self.C2.bind("<Leave>", self.on_leave)
        self.C2.bind("<Motion>", self.MouseOver)
        # self.C2.bind("<Button-1>", self.OnMouseDown)
        self.C2.bind('<B1-Motion>', self.OnMouseDrag)
        self.root.mainloop()  

    def OnMouseDrag(self, event):
        x1 = event.x - self.framew/2 
        x2 = event.x + self.framew/2 
        y1 = event.y - self.frameh/2 
        y2 = event.y + self.frameh/2 

        self.outimg[int(y1):int(y2),int(x1):int(x2),2] = int(self.colorcode[self.framet][2])
        self.outimg[int(y1):int(y2),int(x1):int(x2),1] = int(self.colorcode[self.framet][1])
        self.outimg[int(y1):int(y2),int(x1):int(x2),0] = int(self.colorcode[self.framet][0])

        self.rectpo2 = self.C2.create_rectangle(x1,y1,x2,y2, fill="")
        self.rectpo3 = self.C3.create_rectangle(x1,y1,x2,y2, fill="red", outline="red")


    
    def on_enter(self, event):
        self.rectpo = self.C2.create_rectangle(0, 0, 3, 3, fill="")
        
    def on_leave(self, event):
        self.C2.delete(self.rectpo)
        
        ########################### Mouse Move
    def MouseOver(self, event):
        """Records location of user clicks to establish cropping region"""
        x1 = event.x - self.framew/2 
        x2 = event.x + self.framew/2 
        y1 = event.y - self.frameh/2 
        y2 = event.y + self.frameh/2 
    
        # update rectangle coordinate
        self.C2.coords(self.rectpo, x1,y1,x2,y2)    
            

        ########################### Mouse Click event
    def OnMouseDown(self, event):
        x1 = event.x - self.framew/2 
        x2 = event.x + self.framew/2 
        y1 = event.y - self.frameh/2 
        y2 = event.y + self.frameh/2 
        self.rectpo2 = self.C2.create_rectangle(x1,y1,x2,y2, fill="")

        self.outimg[int(y1):int(y2),int(x1):int(x2),2] = int(self.colorcode[self.framet][2])
        self.outimg[int(y1):int(y2),int(x1):int(x2),1] = int(self.colorcode[self.framet][1])
        self.outimg[int(y1):int(y2),int(x1):int(x2),0] = int(self.colorcode[self.framet][0])
        
        # fromarray = Image.fromarray(np.uint8(self.outimg))
        # outim = ImageTk.PhotoImage(Image.fromarray(np.uint8(self.outimg)))
        # self.C3.delete('all')
        # self.C3.create_image(0,0,anchor="nw",image=outim)


        self.rectpo3 = self.C3.create_rectangle(x1,y1,x2,y2, fill="red", outline="red")

        # cv2.imshow("groundTruth",self.outimg)
        # cv2.imshow(self.window3,self.outimg)
        """Records location of user clicks to establish cropping region"""
        
        
def main():
    root = Tk()
    root.title("Labeling")
    app = ImageEditor(root)

    
if __name__ == '__main__':
    main()