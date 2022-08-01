# You are working on a project for TikTok. The future project will be a web-site of all public GIF images.
# You need to write a function that converts TikTok video to GIF.
# The input parameter is url address of TikTok video, i.e. "TikTok example".
# The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".


from moviepy.editor import *
from pathlib import Path
import os
import random


def convert_to_gif(video_link, start_second, end_second):
    home = str(Path.home())
    num = random.randint(1, 100000)
    file_directory = os.path.join(home, f'TikTok-example-{num}.gif')

    video = VideoFileClip(video_link).subclip(start_second, end_second)
    video.write_gif(file_directory)

    return file_directory


# tiktok_example = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/' \
#                   'tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=' \
#                   '0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=' \
#                   'video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28' \
#                   'vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'

# haven't understood if TikTok example works, tried in all browsers but it didn't work, so took another video link
test_video_link = 'https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'
start_second = 1
end_second = 3

if __name__ == "__main__":
    convert_to_gif(test_video_link, start_second, end_second)
