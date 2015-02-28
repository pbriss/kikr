
# from visual import *
import serial
import string
import math
import pdb
import sys
import re
import numpy
from pylab import *



from time import time, sleep


def main(infilename, outfilename):

    i = 'a'
    makeplot = True

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


                # now do the parsing and plot the data: 
                # re.findall('.*\r(.*)\r',latest_read.replace('$','').replace('#',''))
                #pdb.set_trace()
                accel = re.findall('(\-?\d+),(\-?\d+),(\-?\d+),.*',latest_read.replace('$','').replace('#',''))
                magn  = re.findall('\-?\d+,\-?\d+,\-?\d+,(\-?\d+),(\-?\d+),(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))
                gyro  = re.findall('\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+),(\-?\d+),(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))
        
                accel_x = re.findall('.*(\-?\d+),\-?\d+,\-?\d+,.*\r',latest_read.replace('$','').replace('#',''))
                accel_y = re.findall('.*\-?\d+,(\-?\d+),\-?\d+,.*\r',latest_read.replace('$','').replace('#',''))
                accel_z = re.findall('.*\-?\d+,\-?\d+,(\-?\d+),.*\r',latest_read.replace('$','').replace('#',''))
        
                magn_x = re.findall('.*\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+,\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                magn_y = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                magn_z = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))
        
                gyro_x = re.findall('.*\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+,\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                gyro_y = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+),\-?\d+.*\r',latest_read.replace('$','').replace('#',''))
                gyro_z = re.findall('.*\-?\d+,\-?\d+,\-?\d+,\-?\d+,\-?\d+,(\-?\d+).*\r',latest_read.replace('$','').replace('#',''))

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



    maxval = max([max(abs(diff_x)), max(abs(diff_y)), max(abs(diff_z))])
    factor = 0.4

    maxvalm = max([max(abs(diffm_x)), max(abs(diffm_y)), max(abs(diffm_z))])
    factor = 0.4

    maxvalg = max([max(abs(diffg_x)), max(abs(diffg_y)), max(abs(diffg_z))])
    factor = 0.4
    


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
                    print x



    #pdb.set_trace()
    for x in numpy.nditer(indsg_z_clean):
        print x
        # Get index when it happened: 
        curidx = numpy.nonzero( diffg_z  ==  x )[0] 
        pdb.set_trace()
        fout.write("T=" + str(timearr[x]) +  " Jump" + "\n" )

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

        

# end        

    pdb.set_trace()


def indices(a, func):
    return [i for (i, val) in enumerate(a) if func(val)]



if __name__ == "__main__":


    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)

    val = ''
    if (len(sys.argv) > 3):
        val = sys.argv[3]


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

    if len(sys.argv) > 1:
        infilename = sys.argv[1]
    if len(sys.argv) > 2:
        outfilename = sys.argv[2]

    main(infilename, outfilename)

