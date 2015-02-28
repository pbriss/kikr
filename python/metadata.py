
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


    pdb.set_trace()
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

    maxval = max([max(abs(diff_x)), max(abs(diff_y)), max(abs(diff_z))])
    factor = 0.7
    


    pdb.set_trace()
    inds_x = numpy.nonzero(abs(diff_x)>maxval* factor)
    inds_y = numpy.nonzero(abs(diff_y)>maxval* factor)
    inds_z = numpy.nonzero(abs(diff_z)>maxval* factor)
    
    jumpdet = concatenate([inds_x[0], inds_y[0], inds_z[0]])

    pdb.set_trace()
    for x in numpy.nditer(jumpdet):
        print x
        fout.write("T=" + str(x) )

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


    pdb.set_trace()

    if len(sys.argv) > 1:
        infilename = sys.argv[1]
    if len(sys.argv) > 2:
        outfilename = sys.argv[2]

    main(infilename, outfilename)

