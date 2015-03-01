import os
import signal
from time import sleep
from subprocess import Popen
import pdb

#os.system("ffmpeg -y -i http://10.5.5.9:8080/live/amba.m3u8 -c:v copy -an python/videos/src/test.mp4 &")
#process = Popen("ffmpeg -y -i http://10.5.5.9:8080/live/amba.m3u8 -c:v copy -an python/videos/src/test.mp4", shell=True)

alreadystart = False

# Checking if we need to break our process
#if 0: 
while True:
        

    sleep(1.5)

    try:
        f = open('python/stateserial.txt', 'r')
        strr = f.readline()
        f.close()
    except IOError:
        strr = '0'

    if alreadystart == False:
        if '1' in strr:
            alreadystart = True
            process = Popen("ffmpeg -y -i http://10.5.5.9:8080/live/amba.m3u8 -c:v copy -an python/videos/src/test.mp4", shell=True)
    else:
        if '0' in strr:
            os.kill(process.pid, signal.SIGTERM)
            alreadystart = False
