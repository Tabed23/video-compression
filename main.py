from moviepy.editor import VideoFileClip
from IPython import  display
input_video = "pexels-alexander-jensen-20496059 (1080p).mp4"
output_video = './pexels-alexander-jensen-20496059.mp4'

clip = VideoFileClip(input_video)

target_resolution = (1280, 720)
clip_resized = clip.resize(newsize=target_resolution)

clip_resized.write_videofile(output_video)
