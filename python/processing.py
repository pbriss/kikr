import os
import pdb
import re
import sys

from moviepy.editor import *


def main(isLocal):
    #get the metadata.txt file : 
    f = open('metadata.txt', 'r')
    metaline = f.readline()

    StartNegOffset = 3  # How many seconds before the jump
    ClipLength = 10  # in seconds 

    
    JumpLocation = int(re.findall('T=(\d+)', metaline)[0])
    startclip = JumpLocation - StartNegOffset
    endclip = startclip + ClipLength


    if (isLocal):
        makevideoclip( startclip , endclip , 'videos/segments/jump1')
    else:
        makevideoclip( startclip , endclip , 'python/videos/segments/jump1')        



def makevideoclip(startclip, endclip, fileout):

    # Grab original clip
    video = VideoFileClip('latest.mp4').subclip(startclip, endclip)

    # Create thumbnail
    video.save_frame( fileout + '.png')
    
    result = CompositeVideoClip([video])
    
    # Save and crop segment
    result.write_videofile( fileout + '.mp4', audio=True)



if __name__ == "__main__":



    val = ''
    if (len(sys.argv) > 1):
        val = sys.argv[1]

    isLocal = False
    if val == 'local':
        isLocal =	True
        
    

    main(isLocal)
