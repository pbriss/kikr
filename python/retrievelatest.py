# Python script to get the latest file: 


import os
import glob
import shutil
import pdb


newest = max(glob.iglob('/Volumes/NO NAME/DCIM/100GOPRO/*.[Mm][Pp]4'), key=os.path.getctime)


pdb.set_trace()
shutil.copyfile(newest, 'latest.mp4')

print newest
