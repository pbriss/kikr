import os
import signal
from time import sleep
from subprocess import Popen

process = Popen("ffmpeg -y -i http://10.5.5.9:8080/live/amba.m3u8 -c:v copy -an videos/src/test.mp4", shell=True)

# Checking if we need to break our process
while True:
    sleep(1.5)
    f = open('state.txt', 'r')
    if f.readline() == '0':
        os.kill(process.pid, signal.SIGTERM)
        break
