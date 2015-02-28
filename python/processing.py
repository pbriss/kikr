from moviepy.editor import *

# Grab original clip
video = VideoFileClip('videos/src/sample.mp4').subclip(0, 6)

# Create thumbnail
video.save_frame('videos/segments/thumb1.png')

result = CompositeVideoClip([video])

# Save and crop segment
result.write_videofile('videos/segments/vid1.mp4', audio=True)