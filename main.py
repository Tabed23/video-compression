from moviepy.editor import VideoFileClip
input_video = "./videos/__temp__.mp4"
output_video = './videocompress/__temp__.mp4'

clip = VideoFileClip(input_video)

target_resolution = (1280, 720)
# 60 % reducing the video

clip_resized = clip.resize(0.6)

clip_resized.write_videofile(output_video)
