# import streamlit as st

from pytube import YouTube, Playlist, exceptions

from pydub import AudioSegment

yt = YouTube('https://www.youtube.com/watch?v=I268QTv0G88')

# for stream in yt.streams.filter(only_audio=True):
#     print(stream)
#     stream.get_by_itag(140)

# stream = yt.streams.filter(only_audio=True)
# one = stream.get_by_itag(140)
# one.download(filename_prefix='mp4')
# two = stream.get_by_itag(251)
# two.download(filename_prefix='webm')

# Video
# playlist = 'https://www.youtube.com/playlist?list=PLRg2tbfTDKwHYN-pqtCbKkTgA9JtwnkNj'

# playlist url
# playlist = 'https://www.youtube.com/playlist?list=PLFzsFUO-y0HDWkdsBMtufEThI2I3c9WlZ'

# p = Playlist(playlist)

# for video in p.videos:
#     print(video.title)

# for url in p.video_urls:
#     try:
#         yt = YouTube(url)
#     except exceptions.VideoUnavailable:
#         print(f'Video {url} is unavailable, skipping')
#     else:
#         print(f'Dowloading video: {yt.title}')
#         yt.streams.first().download()


# Convert

# mp4_file = 'webmHimawari Meets Ino  Boruto Naruto Next Generations.webm'
# mp3_file = 'webbm.mp3'

# audiomp3 = AudioSegment.from_file(mp4_file)
# audiomp3.export(mp3_file, format='mp3')
# print('Done')