import os

from moviepy.editor import *

# Grab original clip
video = VideoFileClip('python/videos/src/sample.mp4').subclip(218, 228)

# Create thumbnail
video.save_frame('python/videos/segments/thumb1.png')

result = CompositeVideoClip([video])

# Save and crop segment
result.write_videofile('python/videos/segments/vid1.mp4', audio=True)