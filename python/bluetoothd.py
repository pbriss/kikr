# from visual import *                                                                                                                  
import serial
import string
import math
import pdb
import sys
import re
import os
import signal
from subprocess import Popen
from pylab import *


#from datetime import datetime

import datetime
import time
#import gopro

#from time import time, sleep
#import time, sleep


def main(outfilename, isLocal):


    #beginning_of_test = datetime.datetime.combine(now.date(), datetime.time(0))  

    fser = open('python/stateserial.txt', 'w+')
    fser.write("0")
    fser.close()

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


    print "serialopened"
    now = datetime.datetime.now()
    beginning_of_test = datetime.datetime.now()

    fser = open('python/stateserial.txt', 'w+')
    fser.write("1")
    fser.close()

    #gopro.main()
    #os.system("python python/gopro.py &")
    #os.system("ffmpeg -y -i http://10.5.5.9:8080/live/amba.m3u8 -c:v copy -an python/videos/src/test.mp4 &")
    #process = Popen("ffmpeg -y -i http://10.5.5.9:8080/live/amba.m3u8 -c:v copy -an python/videos/src/test.mp4", shell=True)

    startlog = False

    while True: 

        if startlog == False:
            # Checking if we need to break our process
            time.sleep(1)
            
        if (isLocal):
            f = open('state.txt', 'r')
        else:
            f = open('python/state.txt', 'r')
        statestr = f.readline()
            

        # f = open('state.txt', 'r')
        #if f.readline() == "0":
        if  '2' in statestr:
            ser.close()
            fout.close()
            # os.kill(process.pid, signal.SIGTERM)
            break

        if '0' in statestr:
            if startlog:
                startlog = False
                fout.close()

        if  '1' in statestr:
            if startlog == False:
                fout = open(outfilename, 'w+')

            startlog = True
            read_val = send(ser, "4")
            time.sleep(1)
            read_val = send(ser, "a")
            read_val = readserial(ser)
            latest_read = read_val        


            while read_val != None:
                read_val = readserial(ser)
                if read_val != None:
                    latest_read = latest_read + read_val

            now = datetime.datetime.now()   
            curtime = (now - beginning_of_test).seconds

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














