from PIL import Image

import os
import time
import numpy as np
import math

import pdb


# FilePath = 'C:/Users/JOHN/Dropbox/_ISPL/SmartFactory/Seam_work_full/sangyup_half2/1/GroundTruth/'
# FilePath = 'F:/Dropbox/_ISPL/SmartFactory/Seam_work_full/sangyup_half2/1/GroundTruth/'
FilePath = 'F:/Dropbox/_ISPL/SmartFactory/Seam_work_full/sangyup_half2/1/didit/'

# FilePath = 'F:/Dropbox/_ISPL/SmartFactory/Seam_work_full/190121_stitch_yup_half2/1/didit/'
# FilePath = 'F:/Dropbox/_ISPL/SmartFactory/Seam_work_full/190121_stitch_yup_half2/1/GroundTruth/'

included_extenstions = ['jpg', 'bmp', 'png', 'gif']
imgdirlist = [fn for fn in os.listdir(FilePath)
            if any(fn.endswith(ext) for ext in included_extenstions)]

picn = 16
i=0
prevname = ''

for dirn in range(len(imgdirlist)):
    imgdir = FilePath+'/'+imgdirlist[dirn]
    img = Image.open(imgdir)


    # print(str(dirn) + '/' + str(len(imgdirlist)) + ' : ' + imgdirlist[dirn])

    if i==0:
        new_im = Image.new('RGB', (img.size[0]*4, img.size[1]*4))
    
    new_im.paste(img, ((i%4)*img.size[0], (math.floor(i/4))*img.size[1] ) )
    i=i+1

    if i == picn:
        prev = imgdirlist[dirn]
        outdir = FilePath+'2/'+ prev[0:-7] + '.jpg'
        new_im.save(outdir)
        print(str(dirn) + '/' + str(len(imgdirlist)))
        print(' ' + outdir)
        # pdb.set_trace() ###

        i=0

    
