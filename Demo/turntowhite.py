from PIL import Image

import os
import time
import numpy as np

import pdb


FilePath = 'C:/Users/JOHN/Dropbox/_ISPL/SmartFactory/Seam_work_full/190121_stitch_yup_half2/1/GroundTruth/23/'
# FilePath = 'F:/Dropbox/_ISPL/SmartFactory/Seam_work_full/sangyup_half2/1/GroundTruth3/'

included_extenstions = ['jpg', 'bmp', 'png', 'gif']
imgdirlist = [fn for fn in os.listdir(FilePath)
            if any(fn.endswith(ext) for ext in included_extenstions)]
    
for dirn in range(len(imgdirlist)):
    imgdir = FilePath+'/'+imgdirlist[dirn]
    img = Image.open(imgdir)


    print(str(dirn+1) + '/' + str(len(imgdirlist)) + ' : ' + imgdirlist[dirn])
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            current = img.getpixel((x, y))
            if current < (128, 128, 128):
                pass
                # print(str(x) + ',' + str(y) + ' : ' + str(pix[x,y]))
                # pdb.set_trace()
            else:
                # print(str(x) + ',' + str(y) + ' : ' + str(current))
                # pdb.set_trace()
                img.putpixel((x, y), (255, 255, 255))

    
    outdir = FilePath+'2/'+imgdirlist[dirn]


    img.save(outdir)
    # img.save(FilePath+'/test.gif')
    # pdb.set_trace()