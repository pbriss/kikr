# Python script to get the latest file: 


import os
import glob


newest = max(glob.iglob('/Volumes/NO NAME/DCIM/100GOPRO/*.[Mm][Pp]4'), key=os.path.getctime)



print newest
