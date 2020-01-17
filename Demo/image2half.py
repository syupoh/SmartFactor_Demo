
import os

import math
from PIL import Image
import pdb


from PIL import Image


def dir_image(relevant_path):
    included_extentions = ['jpg', 'bmp', 'png', 'gif', 'JPG']
    
    file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extentions)]

    return file_names


size = 720 # patch size
# size = 512 # patch size
stride = 128 # patch stride
    

def main():

    # maindir = '/media/syup/Toshiba_3TB/SmartFactory/181112_for_simulator(chosen)/'
    # dir_src = maindir + 'Before_extraction/'
    # dir_tgt = maindir + 'Patches2/'

    # maindir = '/media/syup/Toshiba_3TB/SmartFactory/'
    maindir = 'F:/Dropbox/_ISPL/SmartFactory/Seam_work_full/sangyup'
    lastname = ''
    # maindir = '/media/syup/Toshiba_3TB/SmartFactory/181004_BusinessTrip/'
    # lastname = 'Seam_work'

    dir_src = maindir + lastname 
    dir_tgt = dir_src + '_half2/'
    dir_src = dir_src + '/'


    if not os.path.exists(dir_tgt):
        os.mkdir(dir_tgt)

    classlist = os.listdir(dir_src)
    n_classes = len(classlist)

    tgtdir = []
    

    for idx, classname in enumerate(classlist):
        
        imgsrcdir = dir_src + classname + '/'
        imgtgtdir = dir_tgt + classname + '/'
        if not os.path.exists(imgtgtdir):
            os.mkdir(imgtgtdir)

        filenames = dir_image(imgsrcdir)

        # pdb.set_trace()
        for i in range(len(filenames)):

            print('Class:'  + str(idx) + '/' + str(len(classlist)) 
            + ' ' + str(i) + '/' + str(len(filenames)) + ' '  + filenames[i] )

            name = filenames[i]
            im = Image.open(imgsrcdir+name)

            imsz = im.size
            
            ###
            # sizeH = size
            # sizeW = size

            ########### get gcd.
            if imsz[0] > imsz[1]: 
                small = imsz[1] 
            else: 
                small = imsz[0]

            for k in range(1, small+1): 
                if((imsz[0] % k == 0) and (imsz[1] % k == 0) and k < 6): 
                    gcd = k 
            #############

            sizeW = math.floor(imsz[0]/gcd)
            sizeH = math.floor(imsz[1]/gcd)
            
            nW = math.floor(imsz[0]/sizeW)
            nH = math.floor(imsz[1]/sizeH)

            
            print(' HxW=' + str(imsz[1]) +'x' + str(imsz[0]) + ' gcd=' + str(gcd)+ ' sizeHxsizeW='
            + str(sizeH) + 'x' + str(sizeW) + ' nH, nW=' + str(nH) + ', ' + str(nW))

            # pdb.set_trace()
            patn=0
            for H in range(nH):
                for W in range(nW):
                    # crop : (left, top, rigth, bottom)
                    cropImage = im.crop( ((W)*sizeW, (H)*sizeH, (W+1)*sizeW, (H+1)*sizeH ))

                    outname = '{0}{1:s}_{2:02d}.jpg'.format(imgtgtdir, name[0:-4], patn)
                    patn = patn+1

                    cropImage.save(outname)
                    # pdb.set_trace()





''' 
    dir1_1 = dir1 + '1/'
    dir1_2 = dir1 + '2/'
    dir2_1 = dir2 + '1/'
    dir2_2 = dir2 + '2/'

    filenames = dir_image(dir1_1)

    for i in range(len(filenames)):
        name = filenames[i]
        im = Image.open(dir1_1+name)

        imsz = im.size


        nH = math.floor(imsz[0]/size)
        nW = math.floor(imsz[1]/size)

        patn=0
        for H in range(nH):
            for W in range(nW):
                cropImage = im.crop( ((H)*size, (W)*size, (H+1)*size, (W+1)*size ))

                
                outname = '{0}{1:s}_{2:d}.png'.format(dir2_1, name[0:-4], patn)
                patn = patn+1

                cropImage.save(outname)
                # pdb.set_trace()

    filenames = dir_image(dir1_2)

    for i in range(len(filenames)):
        name = filenames[i]
        im = Image.open(dir1_2+name)

        imsz = im.size


        nH = math.floor(imsz[0]/size)
        nW = math.floor(imsz[1]/size)

        patn=0
        for H in range(nH):
            for W in range(nW):
                cropImage = im.crop( ((H)*size, (W)*size, (H+1)*size, (W+1)*size ))

                
                outname = '{0}{1:s}_{2:d}.png'.format(dir2_2, name[0:-4], patn)
                patn = patn+1

                cropImage.save(outname)
                # pdb.set_trace()


 '''

if __name__ == '__main__':
    main()
