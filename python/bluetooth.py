# from visual import *                                                                                                                  
import serial
import string
import math
import pdb
import sys
import re
import os
from pylab import *


#from datetime import datetime

import datetime
import time
import gopro

#from time import time, sleep
#import time, sleep


def main(outfilename, isLocal):


    #beginning_of_test = datetime.datetime.combine(now.date(), datetime.time(0))  



    resport = False
    while (  resport == False):
        # Check your COM port and baud rate                                                                                             
        [resport, ser] = portIsUsable('/dev/tty.RNBT-2230-RNI-SPP')
        time.sleep(1)
        print "Retrying to open port"

    # ser = serial.Serial(port='/dev/tty.RNBT-2230-RNI-SPP',baudrate=57600, timeout=10)                                                 
    if(ser.isOpen() == False):
        ser.open()

    makeplot = False #True

    #pdb.set_trace()    
    fout = open(outfilename, 'w+')

    print "serialopened"
    now = datetime.datetime.now()
    beginning_of_test = datetime.datetime.now()
    #gopro.main()
    os.system("python python/gopro.py &")



    while True: 
        read_val = send(ser, "4")
        time.sleep(1)
        read_val = send(ser, "a")
        read_val = readserial(ser)
        latest_read = read_val        

        # Checking if we need to break our process
        #pdb.set_trace()
        if (isLocal):
            f = open('state.txt', 'r')
        else:
            f = open('python/state.txt', 'r')


        #pdb.set_trace()
        statestr = f.readline()
        # f = open('state.txt', 'r')
        #if f.readline() == "0":
        if  statestr.find('0') != -1:
            ser.close()
            fout.close()
            break

        while read_val != None:
            read_val = readserial(ser)
            if read_val != None:
                latest_read = latest_read + read_val

        now = datetime.datetime.now()   
        curtime = (now - beginning_of_test).seconds

        #pdb.set_trace()

        if latest_read != None:
            #with open( outfilename, "a+") as myfile:
            fout.write("\nT:" + str(curtime) + ":" + latest_read + "\n")
            fout.flush()
                #myflle.flush()

        



def portIsUsable(portName):
    ser = serial.Serial
    try:
        ser = serial.Serial(port=portName ,baudrate=57600, timeout=2)
        # ser = serial.Serial(port=portName)
        return [ True, ser]
    except:
       return [False, ser]



def readserial(ser):
    if ser.isOpen():
        if ser.inWaiting():
            try:
                read_val = ser.read( ser.inWaiting() )
                print read_val
                return read_val

            except serial.serialutil.SerialException:
                print "Error"
            else:
                return ""
        #else:                                                                                                                                              
            #print("Writing 1")                                                                                                                             
            #send(ser,"1")                                                                                                                                  

    else:
        return ""






def send(ser, message):
    if ser.isOpen():
        try:
            ser.write(message)
            return "" # read_val                                                                                                                            

        except serial.serialutil.SerialException:
            print "Error"
            # attempt to reconnect?                                                                                                                         
            # already tried making new serial object                                                                                                        
            # which just fails when trying to open                                                                                                          
            # check if reconnected?                                                                                                                         
        else:
            return ""
    else:
        return ""





if __name__ == "__main__":


    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    val = ''

    if (len(sys.argv) > 2):
        val = sys.argv[2]
    #pdb.set_trace()                                                                                                                                        

    outfilename = 'python/9dofout.txt'
    isLocal = False
    if val == 'local':
        outfilename = '9dofout.txt'
        isLocal =	True

    if len(sys.argv) > 1:
        outfilename = sys.argv[1]

    #pdb.set_trace()
    main(outfilename, val == 'local')














