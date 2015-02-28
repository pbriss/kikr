import os

from moviepy.editor import *

# Grab original clip
video = VideoFileClip('latest.mp4').subclip(2, 4)

# Create thumbnail
video.save_frame('videos/segments/thumb1.png')

result = CompositeVideoClip([video])

# Save and crop segment
result.write_videofile('videos/segments/vid1.mp4', audio=True)
