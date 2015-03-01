import os
import pdb
import re
import sys

from moviepy.editor import *


def main(islocal):
    #get the metadata.txt file :
    if (islocal):
        f = open('metadata.txt', 'r')
    else:
        f = open('python/metadata.txt', 'r')
    metaline = f.readline()

    StartNegOffset = 3  # How many seconds before the jump
    ClipLength = 10  # in seconds

    #JumpLocation = int(re.findall('T=(\d+)', metaline)[0])
    JumpLocation = int(re.findall('(\d+)', metaline)[0])
    if JumpLocation < StartNegOffset: 
        startclip = 0
    else:
        startclip = JumpLocation - StartNegOffset

    endclip = startclip + ClipLength


    if islocal:
        makevideoclip(startclip, endclip, 'videos/segments/jump1', islocal)
    else:
        makevideoclip(startclip, endclip, 'python/videos/segments/jump1', islocal)



def makevideoclip(startclip, endclip, fileout, islocalin):

    # Grab original clip
    if islocalin:
        video = VideoFileClip('videos/src/test.mp4').subclip(startclip, endclip)
    else:
        video = VideoFileClip('python/videos/src/test.mp4').subclip(startclip, endclip)

    # Create thumbnail
    video.save_frame(fileout + '.png')
    
    result = CompositeVideoClip([video])
    
    # Save and crop segment
    result.write_videofile( fileout + '.mp4', audio=True, verbose=False)


    print "DoneVideo"

if __name__ == "__main__":

    val = ''
    if len(sys.argv) > 1:
        val = sys.argv[1]

    islocal = False
    if val == 'local':
        islocal =	True
        
    main(islocal)
