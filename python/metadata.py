
# from visual import *
import serial
import string
import math
import pdb
import sys
import re
import numpy
from pylab import *

import json
import shutil
#import time
from event import Event




#from time import time, sleep
import time


def main(infilename, outfilename, makeplot):

    i = 'a'
    #makeplot = False

    if makeplot:
        ion()
        figure(1)
        line, = plot([ 2, 3, 4 ])
        
        figure(2)
        line, = plot([ 2, 3, 4 ])


    #pdb.set_trace()
    fout = open(outfilename, 'w+')


    accel_x_all = []
    accel_y_all = []
    accel_z_all = []

    magn_x_all = []
    magn_y_all = []
    magn_z_all = []

    gyro_x_all = []
    gyro_y_all = []
    gyro_z_all = []

    timearr = []
 
    max_xval = 100
    max_yval = 100
    max_zval = 100
    min_xval = -100
    min_yval = -100
    min_zval = 0

    curtime = 0

    #f = open('python/9dofout.txt', 'r')
    with open(infilename, "r") as ins:
        array = []
        for line in ins:
            #pdb.set_trace()
            latest_read = line

            if latest_read.find('$') != -1:

                if  len(re.findall('T:(\d+):', latest_read)) > 0:
                    #pdb.set_trace()
                    curtime = int(re.findall('T:(\d+):', latest_read)[0])

                #if curtime == 19:
                    #pdb.set_trace()

                # now do the parsing and plot the data: 
                # re.findall('.*\r(.*)\r',latest_read.replace('$','').replace('#',''))
                #pdb.set_trace()
                accel = re.findall('(\-?\d+),(\-?\d+),(\-?\d+),.*',latest_read.replace('$','').replace('#',''))
                magn  = re.findall('\-?\d+,\-?\d+,\-?\d+,(\-?\d+),(\-?\d+),(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))
                gyro  = re.findall('\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+),(\-?\d+),(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))
        
                #accel_x = re.findall('.*(\-?\d+),\-?\d+,\-?\d+,.*\r',latest_read.replace('$','').replace('#',''))
                #accel_y = re.findall('.*\-?\d+,(\-?\d+),\-?\d+,.*\r',latest_read.replace('$','').replace('#',''))
                #accel_z = re.findall('.*\-?\d+,\-?\d+,(\-?\d+),.*\r',latest_read.replace('$','').replace('#',''))
        
                #magn_x = re.findall('.*\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+,\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                #magn_y = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                #magn_z = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))
        
                #gyro_x = re.findall('.*\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+,\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                #gyro_y = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                #gyro_z = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))

                #pdb.set_trace()
                #accel_x = [accel[0][0]]
                #accel_y = [accel[0][1]]
                #accel_z = [accel[0][2]]

                accel_x = getindexcheck(accel,0)
                accel_y = getindexcheck(accel,1)
                accel_z = getindexcheck(accel,2)

                magn_x = getindexcheck(magn,0)
                #magn_x = [magn[0][0]]
                magn_y = getindexcheck(magn,1)
                magn_z = getindexcheck(magn,2)
                #magn_z = [magn[0][2]]


                gyro_x = getindexcheck(gyro,0)
                gyro_y = getindexcheck(gyro,1)
                gyro_z = getindexcheck(gyro,2)
                #gyro_x = [gyro[0][0]]
                #gyro_y = [gyro[0][1]]
                #gyro_z = [gyro[0][2]]



                #if int(gyro_z[0]) > 0:
                #    pdb.set_trace()
                
                #pdb.set_trace()                
                timearr = timearr + [curtime]

                accel_x_all = accel_x_all + accel_x
                accel_x_all_fl = [float(i) for i in accel_x_all]
                accel_y_all = accel_y_all + accel_y
                accel_y_all_fl = [float(i) for i in accel_y_all]
                accel_z_all = accel_z_all + accel_z
                accel_z_all_fl = [float(i) for i in accel_z_all]

                magn_x_all = magn_x_all + magn_x
                magn_x_all_fl = [float(i) for i in magn_x_all]
                magn_y_all = magn_y_all + magn_y
                magn_y_all_fl = [float(i) for i in magn_y_all]
                magn_z_all = magn_z_all + magn_z
                magn_z_all_fl = [float(i) for i in magn_z_all]

                gyro_x_all = gyro_x_all + gyro_x
                gyro_x_all_fl = [float(i) for i in gyro_x_all]
                gyro_y_all = gyro_y_all + gyro_y
                gyro_y_all_fl = [float(i) for i in gyro_y_all]
                gyro_z_all = gyro_z_all + gyro_z
                gyro_z_all_fl = [float(i) for i in gyro_z_all]



    # ==================================
    # PErform basic detection: 
    # ==================================

    diff_x = numpy.diff(accel_x_all_fl)
    diff_y = numpy.diff(accel_y_all_fl)
    diff_z = numpy.diff(accel_z_all_fl)
    txd = np.arange(0,len(diff_x),1)
    tyd = np.arange(0,len(diff_y),1)
    tzd = np.arange(0,len(diff_z),1)

    diffm_x = numpy.diff(magn_x_all_fl)
    diffm_y = numpy.diff(magn_y_all_fl)
    diffm_z = numpy.diff(magn_z_all_fl)
    txdm = np.arange(0,len(diffm_x),1)
    tydm = np.arange(0,len(diffm_y),1)
    tzdm = np.arange(0,len(diffm_z),1)

    diffg_x = numpy.diff(gyro_x_all_fl)
    diffg_y = numpy.diff(gyro_y_all_fl)
    diffg_z = numpy.diff(gyro_z_all_fl)
    txdg = np.arange(0,len(diffg_x),1)
    tydg = np.arange(0,len(diffg_y),1)
    tzdg = np.arange(0,len(diffg_z),1)

    
    getonlymax = True

    maxval = max([max(abs(diff_x)), max(abs(diff_y)), max(abs(diff_z))])
    factor = 0.6

    maxvalm = max([max(abs(diffm_x)), max(abs(diffm_y)), max(abs(diffm_z))])
    factor = 0.6

    maxvalg = max([max(abs(diffg_x)), max(abs(diffg_y)), max(abs(diffg_z))])
    factor = 0.6
    


    #pdb.set_trace()
    inds_x = numpy.nonzero(abs(diff_x)>maxval* factor)
    inds_y = numpy.nonzero(abs(diff_y)>maxval* factor)
    inds_z = numpy.nonzero(abs(diff_z)>maxval* factor)
    
    jumpdet = concatenate([inds_x[0], inds_y[0], inds_z[0]])


    indsm_x = numpy.nonzero(abs(diffm_x)>maxval* factor)
    indsm_y = numpy.nonzero(abs(diffm_y)>maxval* factor)
    indsm_z = numpy.nonzero(abs(diffm_z)>maxval* factor)
    jumpdetm = concatenate([indsm_x[0], indsm_y[0], indsm_z[0]])

    indsg_x = numpy.nonzero(abs(diffg_x)>maxval* factor)
    indsg_y = numpy.nonzero(abs(diffg_y)>maxval* factor)
    indsg_z = numpy.nonzero(abs(diffg_z)>maxval* factor)
    jumpdetg = concatenate([indsg_x[0], indsg_y[0], indsg_z[0]])


    # Subsampling the Z : (subsample max)
    # Remove the sample close to each other: 
    indsg_z_clean = indsg_z[0]

    if 0: 
        for x in indsg_z_clean:
        #Make sure they are unique: 
            curv = numpy.nonzero( indsg_z_clean  ==  x )[0] 
        #pdb.set_trace()
            
            if len(curv) > 0:
                nonuniquearr = numpy.nonzero(abs(indsg_z_clean-x) < 5 ) 
                for nonunique in nonuniquearr[0]:
                    if nonunique != curv[0]:
                #curelement_index = numpy.nonzero( indsg_z_clean  ==  nonunique )[0] 
                        indsg_z_clean = np.delete(indsg_z_clean,nonunique )
                        #print x

    #indsm_y_clean = subsampleclose(indsm_y, 5)
    #pdb.set_trace()

    #timearr_np[indsm_y[0]].reshape(-1,)

    diffm_x_max = max(diffm_x)
    diffm_y_max = max(diffm_y)
    diffm_z_max = max(diffm_z)
    magnmax = np.argmax([diffm_x_max, diffm_y_max, diffm_z_max])
    
    if magnmax == 0:
        diffmax = indsm_x
    elif magnmax == 1:
        diffmax = indsm_y
    elif magnmax == 2:
        diffmax = indsm_z

    diffg_x_max = max(diffg_x)
    diffg_y_max = max(diffg_y)
    diffg_z_max = max(diffg_z)
    diffg_xyz_max = [diffg_x_max, diffg_y_max, diffg_z_max]
    diffg_x_min = min(diffg_x)
    diffg_y_min = min(diffg_y)
    diffg_z_min = min(diffg_z)
    diffg_xyz_min = [diffg_x_min, diffg_y_min, diffg_z_min]
    maggmax = np.argmax(diffg_xyz_max)

    extreme_gyro =  abs(max(diffg_xyz_max)   - min(diffg_xyz_min))
    


    StartNegOffset = 4  # How many seconds before the jump
    ClipLength = 10  # in seconds

    timearr_np = np.array(timearr)    

    # Getting the index of highest gyro: 
    maxidx = np.argmax(diffg_xyz_max)
    extreme_gyro_idx = timearr_np[maxidx]



    if getonlymax:
        #pdb.set_trace()        
        maxidx = np.argmax(diffm_y)
        timearr_indsm_y_clean = timearr_np[maxidx]
        fout.write(str(timearr_indsm_y_clean) + "\n" )

        if timearr_indsm_y_clean < StartNegOffset: 
            startclip = 0
        else: 
            startclip = timearr_indsm_y_clean - StartNegOffset
        endclip = timearr_indsm_y_clean - StartNegOffset + ClipLength

        delta_xgyro = abs(timearr_indsm_y_clean - extreme_gyro_idx)

        events = list()
        move = "Jump"
        if (extreme_gyro > 200):
            if (delta_xgyro > 3):
                move = "180"

        events.append(Event(startclip, endclip, move, maxidx))
        print json.dumps(events, default=lambda o: o.__dict__)
        


    else:
        #timearr_indsm_y_clean = list(set(timearr_np[indsm_y[0]]))
        timearr_indsm_y_clean = list(set(timearr_np[diffmax[0]]))



    #pdb.set_trace()
        #for x in numpy.nditer(indsm_y_clean):
        for x in timearr_indsm_y_clean:
            #print x
            # Get index when it happened: 
            #pdb.set_trace()
            #fout.write("T=" + str(x) +  " Jump" + "\n" )
            fout.write(str(x) + "\n" )

    fout.close()



    if makeplot:
        tx = np.arange(0,len(accel_x_all_fl),1)
        ty = np.arange(0,len(accel_y_all_fl),1)
        tz = np.arange(0,len(accel_z_all_fl),1)
        txm = np.arange(0,len(magn_x_all_fl),1)
        tym = np.arange(0,len(magn_y_all_fl),1)
        tzm = np.arange(0,len(magn_z_all_fl),1)
        txg = np.arange(0,len(gyro_x_all_fl),1)
        tyg = np.arange(0,len(gyro_y_all_fl),1)
        tzg = np.arange(0,len(gyro_z_all_fl),1)
        
        # pdb.set_trace()
        figure(1)
        clf()
        plot(tx,accel_x_all_fl, ty, accel_y_all_fl, tz, accel_z_all_fl)  
        draw() # update the plot

        #pdb.set_trace()        

        figure(2)
        plot(txm,magn_x_all_fl, tym, magn_y_all_fl, tzm, magn_z_all_fl)
        draw() # update the plot


        figure(3)
        plot(txg, gyro_x_all_fl, tyg, gyro_y_all_fl, tzg, gyro_z_all_fl)
        draw() # update the plot

        #now show detection: 
        figure(4)
        plot(txd, diff_x, tyd, diff_y, tzd, diff_z)
        draw() # update the plot

        figure(5)
        plot(txdm, diffm_x, tydm, diffm_y, tzdm, diffm_z)
        draw() # update the plot

        figure(6)
        plot(txdg, diffg_x, tydg, diffg_y, tzdg, diffg_z)
        draw() # update the plot


        if makeplot:
            pdb.set_trace()

    return [timearr_indsm_y_clean, maxidx]
        

# end        


    #print "Done"

def subsampleclose(arr, distance):
    arr_clean = arr
    
    #pdb.set_trace()
    for x in arr_clean:
        #Make sure they are unique: 
        curv = numpy.nonzero( arr_clean  ==  x )[0] 
        #pdb.set_trace()
    
        if len(curv) > 0:
            nonuniquearr = numpy.nonzero(abs( arr_clean-x) <  distance ) 
            for nonunique in nonuniquearr[0]:
                if nonunique != curv[0]:
                #curelement_index = numpy.nonzero( indsg_z_clean  ==  nonunique )[0] 
                    arr_clean = np.delete(arr_clean,nonunique )
                    print x


    return arr_clean




def getindexcheck(arr,idx):
    if len(arr) > 0:
        if len(arr[0]) > idx:
            return [arr[0][idx]]
        else:
            return []
    else:
        return []



def indices(a, func):
    return [i for (i, val) in enumerate(a) if func(val)]



if __name__ == "__main__":


    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)

    makeplot = False
    if (len(sys.argv) > 1):
        makeplotstr = sys.argv[1]
        if '1' in makeplotstr:
            makeplot = True


    val = ''
    if (len(sys.argv) > 4):
        val = sys.argv[4]


    isLocal = False
    if val == 'local':
        outfilename = '9dofout.txt'
        isLocal =	True
    else:
        #infilename = 'python/9dofout.txt'
        #outfilename = 'python/metadata.txt'
        infilename = 'python/9dofout.txt'
        outfilename = 'python/metadata.txt'


    #pdb.set_trace()

    if len(sys.argv) > 2:
        infilename = sys.argv[2]
    if len(sys.argv) > 3:
        outfilename = sys.argv[3]

    try:
        
        [detoffset, maxidx] = main(infilename, outfilename, makeplot)

    # Now copy the file for logging purposes: 
        #pdb.set_trace()
        now_timestamp = time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime())
        bu_filename = infilename.replace(".txt","_" + now_timestamp + "_D" + str(detoffset) +  ".txt")
        shutil.copyfile(infilename, bu_filename)

    except:
        events = list()
        events.append(Event(0, 10, "180", -1))
        print json.dumps(events, default=lambda o: o.__dict__)


